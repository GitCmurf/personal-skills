#!/usr/bin/env python3
"""Report whether registered public upstreams have moved.

This command is deliberately read-only. It detects updates; it never downloads,
merges, or rewrites a personal skill.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "registry" / "upstreams.json"


def remote_head(repository: str, branch: str) -> str:
    result = subprocess.run(
        ["git", "ls-remote", repository, f"refs/heads/{branch}"],
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or "git ls-remote failed"
        raise RuntimeError(message)
    line = result.stdout.strip()
    if not line:
        raise RuntimeError(f"branch {branch!r} was not found")
    return line.split()[0]


def check_sources(offline: bool) -> list[dict[str, Any]]:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    reports: list[dict[str, Any]] = []
    for source_id, source in sorted(registry["sources"].items()):
        report: dict[str, Any] = {
            "id": source_id,
            "onboarding": source["onboarding"],
            "recorded_head": source["tracked_head"],
            "repository": source["repository"],
        }
        if offline:
            report["status"] = "recorded"
        else:
            try:
                current = remote_head(source["repository"], source["default_branch"])
                report["remote_head"] = current
                report["status"] = "current" if current == source["tracked_head"] else "update-available"
            except (OSError, RuntimeError, subprocess.SubprocessError) as error:
                report["status"] = "error"
                report["error"] = str(error)
        reports.append(report)
    return reports


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true", help="validate and report recorded state only")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument(
        "--fail-on-update",
        action="store_true",
        help="return exit status 3 when an upstream update is available",
    )
    args = parser.parse_args()

    reports = check_sources(args.offline)
    payload = {"mode": "offline" if args.offline else "live", "sources": reports}
    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        for report in reports:
            print(f"{report['id']}: {report['status']}")

    if any(report["status"] == "error" for report in reports):
        return 2
    if args.fail_on_update and any(report["status"] == "update-available" for report in reports):
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
