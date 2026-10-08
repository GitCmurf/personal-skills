"""Classify a saved CodeRabbit review stream without printing repository content."""

import argparse
import json
from pathlib import Path


def classify(stdout: str, exit_code: int) -> dict:
    findings = 0
    completions = []
    errors = False
    malformed = False
    after_completion = False
    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except (ValueError, TypeError):
            malformed = True
            continue
        if not isinstance(event, dict) or not isinstance(event.get("type"), str):
            malformed = True
            continue
        if event["type"] == "error":
            errors = True
        if event.get("phase") == "auth":
            continue  # Authentication completion is not review completion.
        if completions:
            after_completion = True
        if event["type"] == "finding":
            findings += 1
        elif event["type"] == "complete":
            completions.append(event)

    result = {"classification": "incomplete", "findings": findings,
              "review_exit_code": exit_code}
    if exit_code != 0 or errors or malformed or after_completion or len(completions) != 1:
        return result
    complete = completions[0]
    count = complete.get("findings")
    uncovered = complete.get("unreviewedFileCount", 0)
    if (type(count) is not int or count != findings or
            type(uncovered) is not int or uncovered != 0):
        return result
    outcome = complete.get("outcome")
    if outcome not in (None, "completed", "completed_with_warnings"):
        return result
    status = complete.get("status")
    message = complete.get("message", "")
    if status == "review_skipped" and findings == 0:
        result["classification"] = "skipped"
    elif status == "review_completed":
        if isinstance(message, str) and message.startswith(
                "No fresh detailed file review was performed in this run."):
            result["classification"] = "skipped"
        else:
            result["classification"] = "completed"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stdout_file", type=Path)
    parser.add_argument("--exit-code", type=int, required=True,
                        help="Actual review process exit code, not a later shell command")
    args = parser.parse_args()
    try:
        result = classify(args.stdout_file.read_text(encoding="utf-8"), args.exit_code)
    except (OSError, UnicodeError):
        result = {"classification": "incomplete", "reason": "unreadable_stdout"}
    print(json.dumps(result))
    return 0 if result["classification"] == "completed" else 2


if __name__ == "__main__":
    raise SystemExit(main())
