#!/usr/bin/env python3
"""Behavioral tests for the loop-research retrieval adapter."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


SCRIPT = Path(__file__).with_name("insane-search-fallback.py")


class InsaneSearchFallbackBehavior(unittest.TestCase):
    def test_it_reports_unavailable_when_no_backend_is_configured(self) -> None:
        """Given no backend, When fallback is requested, Then it fails explicitly."""
        with tempfile.TemporaryDirectory() as temp_dir:
            env = os.environ.copy()
            env["INSANE_SEARCH_ROOT"] = str(Path(temp_dir) / "missing")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "https://example.com", "--json"],
                env=env, capture_output=True, text=True, check=False,
            )

        self.assertEqual(result.returncode, 2)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["status"], "unavailable")
        self.assertFalse(payload["ok"])

    def test_it_passes_the_url_and_options_to_the_backend(self) -> None:
        """Given an installed backend, When fallback runs, Then its CLI receives the request."""
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "insane-search"
            engine = root / "engine"
            engine.mkdir(parents=True)
            (engine / "__main__.py").write_text(
                textwrap.dedent(
                    """
                    import sys
                    print("[BEGIN UNTRUSTED WEB CONTENT]")
                    print("url=" + sys.argv[1])
                    print("device=" + sys.argv[sys.argv.index('--device') + 1])
                    print("selector=" + sys.argv[sys.argv.index('--selector') + 1])
                    print("[END UNTRUSTED WEB CONTENT]")
                    """
                ), encoding="utf-8",
            )
            env = os.environ.copy()
            env["INSANE_SEARCH_ROOT"] = str(root)
            result = subprocess.run(
                [
                    sys.executable, str(SCRIPT), "https://blocked.example/article",
                    "--device", "mobile", "--selector", "article", "--json",
                ], env=env, capture_output=True, text=True, check=False,
            )

        self.assertEqual(result.returncode, 0)
        payload = json.loads(result.stdout)
        self.assertTrue(payload["ok"])
        self.assertIn("url=https://blocked.example/article", payload["content"])
        self.assertIn("device=mobile", payload["content"])
        self.assertIn("selector=article", payload["content"])

    def test_it_rejects_non_public_url_schemes_before_backend_execution(self) -> None:
        """Given a non-http URL, When fallback runs, Then it rejects it before execution."""
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "file:///etc/passwd", "--json"],
            capture_output=True, text=True, check=False,
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("http://", result.stderr)


if __name__ == "__main__":
    unittest.main()
