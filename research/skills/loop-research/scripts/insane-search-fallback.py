#!/usr/bin/env python3
"""Run the installed insane-search engine as a public-source fallback."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlparse


BACKEND_ENV = "INSANE_SEARCH_ROOT"
PYTHON_ENV = "INSANE_SEARCH_PYTHON"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Use an installed insane-search engine for blocked public URLs."
    )
    parser.add_argument("url", help="Public http(s) URL to retrieve.")
    parser.add_argument(
        "--selector", action="append", default=[],
        help="Positive-proof CSS selector; repeat for multiple selectors.",
    )
    parser.add_argument("--device", choices=("auto", "desktop", "mobile"), default="auto")
    parser.add_argument("--timeout", type=int, default=25)
    parser.add_argument("--max-attempts", type=int, default=None)
    parser.add_argument("--trace", action="store_true")
    parser.add_argument(
        "--json", action="store_true",
        help="Wrap untrusted content and execution metadata in JSON.",
    )
    return parser


def _valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _candidate_roots() -> list[Path]:
    candidates: list[Path] = []
    configured = os.environ.get(BACKEND_ENV)
    if configured:
        # An explicit path is an override, not merely another hint. This keeps
        # deployments deterministic when multiple agent installations exist.
        return [Path(configured).expanduser().resolve()]

    search_bases = [Path.cwd(), Path(__file__).resolve().parents[4], Path.home()]
    for base in search_bases:
        candidates.extend(
            [
                base / ".agents" / "skills" / "insane-search",
                base / ".claude" / "skills" / "insane-search",
            ]
        )

    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(resolved)
    return unique


def find_backend() -> Path | None:
    for root in _candidate_roots():
        if (root / "engine" / "__main__.py").is_file():
            return root
    return None


def _command(args: argparse.Namespace) -> list[str]:
    python = os.environ.get(PYTHON_ENV, sys.executable)
    command = [python, "-m", "engine", args.url, "--device", args.device]
    for selector in args.selector:
        command.extend(["--selector", selector])
    command.extend(["--timeout", str(args.timeout)])
    if args.max_attempts is not None:
        command.extend(["--max-attempts", str(args.max_attempts)])
    if args.trace:
        command.append("--trace")
    return command


def _emit_unavailable(args: argparse.Namespace) -> int:
    payload = {
        "backend": "insane-search",
        "status": "unavailable",
        "ok": False,
        "content": "",
        "reason": (
            f"No engine installation found. Set {BACKEND_ENV} to the upstream "
            "skill directory if it is installed outside the standard locations."
        ),
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(payload["reason"], file=sys.stderr)
    return 2


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not _valid_url(args.url):
        print("URL must use http:// or https:// and include a host.", file=sys.stderr)
        return 2
    if args.timeout <= 0 or (args.max_attempts is not None and args.max_attempts <= 0):
        print("timeout and max-attempts must be positive.", file=sys.stderr)
        return 2

    root = find_backend()
    if root is None:
        return _emit_unavailable(args)

    try:
        completed = subprocess.run(
            _command(args), cwd=root, capture_output=True, text=True, check=False
        )
    except (OSError, subprocess.SubprocessError) as error:
        if args.json:
            print(json.dumps({
                "backend": "insane-search", "status": "error", "ok": False,
                "content": "", "backend_root": str(root),
                "error": f"{type(error).__name__}: {error}",
            }, ensure_ascii=False, indent=2))
        else:
            print(f"insane-search engine failed to start: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({
            "backend": "insane-search",
            "status": "ok" if completed.returncode == 0 else "failed",
            "ok": completed.returncode == 0,
            "content": completed.stdout,
            "stderr": completed.stderr,
            "backend_root": str(root),
            "exit_code": completed.returncode,
        }, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(completed.stdout)
        sys.stderr.write(completed.stderr)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
