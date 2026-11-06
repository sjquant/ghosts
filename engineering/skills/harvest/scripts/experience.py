#!/usr/bin/env python3
"""Support engineering experience skills with local collection and validation."""

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote, urlsplit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default=os.environ.get("EXPERIENCE_CONFIG"))
    sub = parser.add_subparsers(dest="command", required=True)
    collect_parser = sub.add_parser("collect")
    collect_parser.add_argument("--days", type=int, choices=[7, 30])
    collect_parser.add_argument("--start")
    collect_parser.add_argument("--end")
    collect_parser.add_argument("--sources", nargs="+")
    collect_parser.add_argument("--dry-run", action="store_true")
    save_parser = sub.add_parser("save")
    save_parser.add_argument("--packet", required=True)
    save_parser.add_argument("--decisions", required=True)
    save_parser.add_argument("--dry-run", action="store_true")
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("paths", nargs="+")
    install_parser = sub.add_parser("install")
    install_parser.add_argument("--skills-dir", required=True)
    install_parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            result = validate([Path(p).expanduser() for p in args.paths])
        elif args.command == "install":
            result = install(Path(args.skills_dir).expanduser(), args.dry_run)
        else:
            if not args.config:
                raise ValueError("Supply --config or EXPERIENCE_CONFIG")
            config = json.loads(Path(args.config).expanduser().read_text())
            if args.command == "collect":
                end = timestamp(args.end) if args.end else dt.datetime.now(dt.timezone.utc)
                start = timestamp(args.start) if args.start else end - dt.timedelta(
                    days=args.days or config.get("default_days", 7))
                if start >= end:
                    raise ValueError("start must precede end (interval is [start, end))")
                result = collect(config, start, end, args.sources)
            else:
                packet = json.loads(Path(args.packet).read_text())
                decisions = json.loads(Path(args.decisions).read_text())
                result = save(config, packet, decisions, args.dry_run)
        print(json.dumps(scrub(result), ensure_ascii=False, indent=2))
        return int(bool(result.get("errors")))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({"errors": [redact(str(exc))]}))
        return 1


def collect(config, start, end, selected=None):
    """Collect changed source records without persisting source content."""
    result = {"start": start.isoformat(), "end": end.isoformat(), "records": [],
              "errors": [], "excluded": 0, "sources": {}}
    checkpoint = load_state(notes_root(config) / ".harvest-state.json") if config.get("vault") else {}
    for source in selected or config.get("sources", []):
        count = 0
        try:
            if source == "github":
                records = github_records(config, start, end, result)
            elif source in {"codex", "claude", "agy"}:
                records = session_records(config, source, start, end, result)
            else:
                raise ValueError(f"Unsupported source: {source}")
            for record in records:
                record = scrub(record)
                record["revision"] = digest(record)
                count += 1
                if checkpoint.get(record["id"]) == record["revision"]:
                    result["excluded"] += 1
                else:
                    result["records"].append(record)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            result["errors"].append(f"{source}: {exc}")
        result["sources"][source] = count
    return result


def session_records(config, source, start, end, report):
    roots = config.get("session_roots", {}).get(source, [])
    if not roots:
        raise ValueError(f"No session_roots configured for {source}")
    seen = set()
    for raw_root in roots:
        root = absolute(raw_root)
        if not root.is_dir():
            report["errors"].append(f"{source}: missing directory {root}")
            continue
        pattern = "brain/*/.system_generated/logs/transcript.jsonl" if source == "agy" else "**/*.jsonl"
        files = sorted(root.glob(pattern))
        if source == "agy":
            supported = {p.parents[2].name for p in files}
            for p in sorted((root / "conversations").glob("*")):
                if p.is_file() and p.stem not in supported:
                    report["errors"].append(f"agy: unsupported conversation without transcript: {p.name}")
        for path in files:
            if path.resolve() in seen:
                continue
            seen.add(path.resolve())
            try:
                messages, session, repository = [], path.stem, None
                recognized = False
                for index, line in enumerate(path.read_text().splitlines(), 1):
                    row = json.loads(line)
                    if source == "codex":
                        recognized |= row.get("type") in {"session_meta", "response_item", "event_msg", "turn_context"}
                    elif source == "claude":
                        recognized |= row.get("type") in {"user", "assistant", "system", "file-history-snapshot"}
                    else:
                        recognized |= "step_index" in row and "created_at" in row
                    if source == "codex" and row.get("type") == "session_meta":
                        session = row["payload"].get("id", session)
                    session = row.get("sessionId", session)
                    when = row.get("timestamp") or row.get("created_at")
                    if not when or not start <= timestamp(when) < end:
                        continue
                    text, role = message_text(source, row)
                    if text.strip():
                        messages.append({"locator": f"line:{index}", "role": role,
                                         "timestamp": when, "text": text})
                if path.stat().st_size and not recognized:
                    raise ValueError("Unsupported session schema")
                if messages:
                    if source == "agy":
                        session = path.parents[2].name
                    elif source == "claude" and "subagents" in path.parts:
                        session = f"{session}:{path.stem}"
                    yield {"id": f"{source}:{session}", "source": source,
                           "repository": repository, "source_refs": [path.resolve().as_uri()],
                           "messages": messages}
            except (OSError, ValueError, KeyError, TypeError) as exc:
                report["errors"].append(f"{source}: {path}: {exc}")


def message_text(source, row):
    if source == "codex":
        payload = row.get("payload", {})
        if row.get("type") != "response_item":
            return "", ""
        kind, role = payload.get("type"), payload.get("role")
        if kind == "function_call_output":
            return str(payload.get("output", "")), "tool"
        if kind != "message" or role not in {"user", "assistant"}:
            return "", ""
        return content_text(payload.get("content", [])), role
    if source == "claude":
        if row.get("type") not in {"user", "assistant"}:
            return "", ""
        return content_text(row.get("message", {}).get("content", [])), row["type"]
    if row.get("source") not in {"USER_EXPLICIT", "MODEL"}:
        return "", ""
    return row.get("content", ""), row.get("source", "")


def content_text(content):
    if isinstance(content, str):
        return content
    parts = []
    for block in content:
        if block.get("type") in {"text", "input_text", "output_text"}:
            parts.append(block.get("text", ""))
        elif block.get("type") == "tool_result":
            parts.append(content_text(block.get("content", [])))
    return "\n".join(parts)


def github_records(config, start, end, report):
    login = config.get("github_login")
    if not login:
        raise ValueError("github_login is required; do not infer reviewer identity")
    repos = set(config.get("github_repositories", []))
    for org in config.get("github_organizations", []):
        try:
            repos.update(r["full_name"] for r in gh_pages(f"orgs/{org}/repos?per_page=100"))
        except ValueError as exc:
            report["errors"].append(f"github organization {org}: {exc}")
    for repo in sorted(repos):
        try:
            if not re.fullmatch(r"[\w.-]+/[\w.-]+", repo):
                raise ValueError("Invalid repository name")
            since = start.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z")
            comments = gh_pages(f"repos/{repo}/pulls/comments?since={since}&per_page=100")
            pulls = gh_pages(f"repos/{repo}/pulls?state=all&sort=updated&direction=desc&per_page=100")
            relevant = {p["number"]: p for p in pulls if timestamp(p["updated_at"]) >= start}
            for comment in comments:
                if comment.get("user", {}).get("login", "").casefold() != login.casefold():
                    continue
                number = int(comment["pull_request_url"].rsplit("/", 1)[1])
                if number not in relevant:
                    relevant[number] = gh_one(f"repos/{repo}/pulls/{number}")
            for number, pr in relevant.items():
                if pr["user"]["login"].casefold() == login.casefold():
                    report["excluded"] += 1
                    continue
                try:
                    reviews = gh_pages(f"repos/{repo}/pulls/{number}/reviews?per_page=100")
                    own = [c for c in comments if int(c["pull_request_url"].rsplit("/", 1)[1]) == number]
                    for kind, rows in [("comment", own), ("review", reviews)]:
                        for row in rows:
                            when = row.get("updated_at") or row.get("submitted_at") or row.get("created_at")
                            body = row.get("body") or ""
                            if (row.get("user", {}).get("login", "").casefold() != login.casefold()
                                    or not when or not start <= timestamp(when) < end
                                    or not body.strip()
                                    or re.fullmatch(r"(?i)\s*(lgtm|approved?|thanks|👍)[.!\s]*", body)):
                                report["excluded"] += 1
                                continue
                            yield {"id": f"github:{repo}:{kind}:{row['id']}", "source": "github",
                                   "repository": repo, "source_refs": [row["html_url"]],
                                   "adoption": "unverified", "pr": number,
                                   "head_sha": pr["head"]["sha"],
                                   "messages": [{"role": "reviewer", "timestamp": when,
                                                 "text": body, "diff_hunk": row.get("diff_hunk"),
                                                 "commit_id": row.get("commit_id"),
                                                 "path": row.get("path")} ]}
                except (ValueError, KeyError, TypeError) as exc:
                    report["errors"].append(f"github {repo} PR {number}: {exc}")
        except (ValueError, KeyError, TypeError) as exc:
            report["errors"].append(f"github {repo}: {exc}")


def gh_pages(endpoint):
    return [row for page in gh(endpoint, pages=True) for row in page]


def gh_one(endpoint):
    return gh(endpoint, pages=False)


def gh(endpoint, pages):
    command = ["gh", "api", "--method", "GET", endpoint]
    if pages:
        command += ["--paginate", "--slurp"]
    for attempt in range(3):
        try:
            result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise ValueError(f"GitHub request unavailable: {exc}") from exc
        if result.returncode == 0:
            return json.loads(result.stdout)
        if not re.search(r"429|rate limit|HTTP 5\d\d", result.stderr, re.I) or attempt == 2:
            raise ValueError(redact(result.stderr.strip()))
        time.sleep(2 ** attempt)
    raise ValueError("GitHub request failed")


def save(config, packet, decisions, dry_run=False):
    """Save evaluated candidates and acknowledge only successful source revisions."""
    root = notes_root(config)
    records = {r["id"]: r for r in packet["records"]}
    result = {"added": 0, "updated": 0, "skipped": 0, "errors": [], "source_ids": []}
    if dry_run:
        lock = contextlib.nullcontext()
    else:
        root.mkdir(parents=True, exist_ok=True)
        lock = file_lock(root / ".harvest.lock")
    with lock:
        state_path = root / ".harvest-state.json"
        state = load_state(state_path)
        for decision in decisions:
            try:
                record = records[decision["id"]]
                if decision["revision"] != record["revision"]:
                    raise ValueError("Stale source revision")
                if state.get(record["id"]) == record["revision"]:
                    result["skipped"] += 1
                    continue
                for candidate in decision["candidates"]:
                    action = save_candidate(root, candidate, record, dry_run)
                    result[action] += 1
                if not dry_run:
                    state[record["id"]] = record["revision"]
                    atomic_write(state_path, json.dumps(state, indent=2) + "\n")
                result["source_ids"].append(record["id"])
            except (ValueError, KeyError, TypeError, OSError) as exc:
                result["errors"].append(f"{decision.get('id')}: {exc}")
    return result


def save_candidate(root, candidate, record, dry_run):
    candidate = dict(candidate)
    expected = candidate.pop("expected_sha256", None)
    for reserved in {"id", "status", "captured_at", "updated_at", "source_refs", "source_ids"}:
        candidate.pop(reserved, None)
    body = candidate.pop("body")
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    identity = [candidate.get("scope"), candidate.get("repository"), candidate.get("key")]
    candidate.update(id="candidate-" + digest(identity)[:24], status="candidate",
                     captured_at=now, updated_at=now, source_refs=record["source_refs"],
                     source_ids=[record["id"]])
    validate_candidate(candidate, body)
    matches = list(root.glob(f"inbox/*/{candidate['id']}.md"))
    target = root / "inbox" / now[:7] / f"{candidate['id']}.md"
    action = "added"
    if len(matches) > 1:
        raise ValueError(f"Duplicate candidate ID: {candidate['id']}")
    if matches:
        target = matches[0]
        original = target.read_text()
        previous, previous_body = parse_note(original)
        # A retry after a partial failure must not overwrite or duplicate a note.
        same = (all(previous.get(k) == candidate.get(k) for k in
                    ["key", "title", "summary", "type", "scope", "repository", "confidence"])
                and previous_body.strip() == body.strip()
                and record["id"] in previous.get("source_ids", [])
                and set(record["source_refs"]).issubset(previous.get("source_refs", [])))
        if same:
            return "skipped"
        if expected != hashlib.sha256(original.encode()).hexdigest():
            raise ValueError(f"Read existing note and supply expected_sha256: {target}")
        candidate = {**previous, **candidate, "captured_at": previous["captured_at"],
                     "status": previous["status"],
                     "source_ids": sorted(set(previous["source_ids"] + candidate["source_ids"])),
                     "source_refs": sorted(set(previous["source_refs"] + candidate["source_refs"]))}
        action = "updated"
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError("Candidate destination escapes the notes directory")
    note = format_note(candidate, body)
    if redact(note) != note:
        raise ValueError("Potential sensitive information in candidate; remove it before saving")
    if not dry_run:
        atomic_write(target, note)
    return action


def validate(paths):
    """Check candidate contracts, navigation links and Markdown size."""
    result = {"checked": 0, "errors": [], "warnings": []}
    seen = {}
    for path in paths:
        if not path.exists():
            result["errors"].append(f"Missing path: {path}")
            continue
        files = sorted(path.rglob("*.md")) if path.is_dir() else [path]
        graph = {}
        for file in files:
            try:
                text = file.read_text()
                result["checked"] += 1
                if len(text.splitlines()) > 100:
                    result["warnings"].append(f"{file}: exceeds 100 lines; consider a subindex or topic split")
                if redact(text) != text:
                    raise ValueError("Potential sensitive information")
                if text.startswith("---\n") and re.search(r"(?m)^id:", text.split("\n---\n", 1)[0]):
                    meta, body = parse_note(text)
                    if "id" in meta:
                        validate_candidate(meta, body)
                        if meta["id"] in seen:
                            raise ValueError(f"Duplicate ID also in {seen[meta['id']]}")
                        seen[meta["id"]] = str(file)
                graph[file.resolve()] = []
                for target in markdown_links(text):
                    target = target.strip("<>")
                    parsed = urlsplit(target)
                    if parsed.scheme or target.startswith("#"):
                        continue
                    if target.startswith("/"):
                        raise ValueError(f"Use relative navigation links: {target}")
                    destination = file.parent / unquote(parsed.path)
                    if not destination.is_file():
                        raise ValueError(f"Broken relative link: {target}")
                    graph[file.resolve()].append(destination.resolve())
            except (OSError, ValueError, KeyError, TypeError) as exc:
                result["errors"].append(f"{file}: {exc}")
        entry = (path / "INDEX.md").resolve()
        if path.is_dir() and entry in graph:
            reached, pending = set(), [entry]
            while pending:
                current = pending.pop()
                if current not in reached:
                    reached.add(current)
                    pending.extend(graph.get(current, []))
            for orphan in sorted(set(graph) - reached):
                result["warnings"].append(f"{orphan}: not reachable from root INDEX.md")
    return result


def markdown_links(text):
    text = re.sub(r"(?ms)^(```|~~~).*?^\1[^\n]*$", "", text)
    inline = re.findall(r"\[[^\]]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text)
    references = re.findall(r"(?m)^\s{0,3}\[[^\]]+\]:\s+<?([^\s>]+)>?", text)
    return inline + references


def validate_candidate(meta, body):
    required = ["id", "key", "title", "summary", "type", "scope", "repository", "status",
                "confidence", "captured_at", "updated_at", "source_refs", "source_ids"]
    if any(key not in meta for key in required):
        raise ValueError("Missing candidate fields")
    for key in ["key", "title", "summary"]:
        if not isinstance(meta[key], str) or not meta[key].strip():
            raise ValueError(f"Invalid {key}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta["key"]):
        raise ValueError("key must be a stable lowercase slug")
    enums = {"type": {"principle", "decision", "pitfall", "playbook", "snippet"},
             "scope": {"global", "repository"},
             "status": {"candidate", "review", "proposed", "promoted", "skipped"},
             "confidence": {"low", "medium", "high"}}
    for key, values in enums.items():
        if meta[key] not in values:
            raise ValueError(f"Invalid {key}")
    if meta["scope"] == "global" and meta["repository"] is not None:
        raise ValueError("global scope requires repository: null")
    if meta["scope"] == "repository" and not re.fullmatch(r"[\w.-]+/[\w.-]+", meta["repository"] or ""):
        raise ValueError("repository scope requires owner/repo")
    expected = "candidate-" + digest([meta["scope"], meta["repository"], meta["key"]])[:24]
    if meta["id"] != expected:
        raise ValueError("Candidate ID does not match scope/repository/key")
    for key in ["captured_at", "updated_at"]:
        timestamp(meta[key])
    for key in ["source_refs", "source_ids"]:
        if not isinstance(meta[key], list) or not meta[key] or not all(isinstance(v, str) and v for v in meta[key]):
            raise ValueError(f"Invalid {key}")
    if meta["status"] in {"proposed", "promoted"}:
        targets = meta.get("targets")
        if not isinstance(targets, list) or not targets:
            raise ValueError("proposed/promoted requires targets")
        for target in targets:
            if not isinstance(target, str) or Path(target).is_absolute() or ".." in Path(target).parts:
                raise ValueError("targets must stay inside the library")
    for section in ["When", "Principle", "Why", "Limits", "Evidence", "Observation", "Inference"]:
        match = re.search(rf"(?m)^## {section}\s*\n(.+?)(?=\n## |\Z)", body, re.S)
        if not match or not match[1].strip():
            raise ValueError(f"Missing or empty section: {section}")


def parse_note(text):
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("Expected frontmatter with one JSON value per field")
    header, body = text[4:].split("\n---\n", 1)
    meta = {}
    for line in header.splitlines():
        key, value = line.split(":", 1)
        if key in meta:
            raise ValueError(f"Duplicate frontmatter field: {key}")
        meta[key] = json.loads(value)
    return meta, body


def format_note(meta, body):
    return "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}"
                                for key, value in meta.items()) + "\n---\n" + body.strip() + "\n"


def install(destination, dry_run=False):
    """Link the three skills to their shared source without replacing existing skills."""
    result = {"links": [], "errors": []}
    source = Path(__file__).resolve().parents[2]
    # Preflight every target before creating any links.
    for name in ["harvest", "curate", "recall"]:
        target = destination / name
        original = source / name
        if target.is_symlink() and target.resolve() == original:
            continue
        if target.exists() or target.is_symlink():
            raise ValueError(f"Existing skill left untouched: {target}")
        result["links"].append({"source": str(original), "target": str(target)})
    if not dry_run:
        destination.mkdir(parents=True, exist_ok=True)
        for link in result["links"]:
            Path(link["target"]).symlink_to(link["source"], target_is_directory=True)
    return result


def notes_root(config):
    root = absolute(config["vault"])
    relative = Path(config.get("notes_directory", "agent-notes"))
    if relative.is_absolute() or ".." in relative.parts:
        raise ValueError("notes_directory must stay inside the vault")
    target = (root / relative).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("notes_directory escapes the vault through a symlink")
    return target


def absolute(value):
    path = Path(value).expanduser()
    if not path.is_absolute():
        raise ValueError(f"Expected an absolute or ~ path: {value}")
    return path


def timestamp(value):
    parsed = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Timestamps require an explicit timezone")
    return parsed


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def redact(text):
    patterns = [r"(?i)\b(?:gh[pousr]_[A-Za-z0-9_]{16,}|github_pat_[A-Za-z0-9_]{16,}|sk-[A-Za-z0-9_-]{16,}|AKIA[A-Z0-9]{16})\b",
                r"(?im)\b(?:api[_-]?key|access[_-]?token|password|secret)\s*[=:]\s*[\"']?[^\s\"',}]+",
                r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\s\S]*?-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
                r"(?i)Authorization[\"']?\s*[:=]\s*[\"']?(?:Bearer|Basic)\s+[^\s\"']+",
                r"https?://[^\s/:]+:[^\s/@]+@[^\s]+"]
    for pattern in patterns:
        text = re.sub(pattern, "[REDACTED]", text)
    return text


def scrub(value):
    if isinstance(value, str):
        return redact(value)
    if isinstance(value, list):
        return [scrub(item) for item in value]
    if isinstance(value, dict):
        return {key: scrub(item) for key, item in value.items()}
    return value


def load_state(path):
    return json.loads(path.read_text()) if path.exists() else {}


@contextlib.contextmanager
def file_lock(path):
    with path.open("a") as handle:
        os.chmod(path, 0o600)
        fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.resolve().is_relative_to(path.parent.resolve()):
        raise ValueError(f"Refusing symlink outside destination: {path}")
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".experience-")
    try:
        with os.fdopen(fd, "w") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


if __name__ == "__main__":
    sys.exit(main())
