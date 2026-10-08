import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/code-review/scripts/review_outcome.py"
spec = importlib.util.spec_from_file_location("review_outcome", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def stream(*events):
    return "\n".join(json.dumps(event) for event in events)


def complete(**fields):
    return {"type": "complete", "status": "review_completed", "findings": 0, **fields}


class ReviewOutcomeTests(unittest.TestCase):
    def test_complete_zero_and_nonzero_findings(self):
        for events, count in (([complete()], 0),
                              ([{"type": "finding", "severity": "major"},
                                complete(findings=1)], 1)):
            with self.subTest(count=count):
                result = module.classify(stream(*events), 0)
                self.assertEqual("completed", result["classification"])
                self.assertEqual(count, result["findings"])

    def test_failed_partial_and_unrecognised_outcomes(self):
        for fields in ({"outcome": "failed"}, {"unreviewedFileCount": 1},
                       {"outcome": "new_unknown_state"}, {"findings": 2},
                       {"findings": True}, {"unreviewedFileCount": "0"},
                       {"status": "authenticated"}):
            with self.subTest(fields=fields):
                self.assertEqual("incomplete", module.classify(
                    stream(complete(**fields)), 0)["classification"])

    def test_warnings_with_full_coverage_can_complete(self):
        self.assertEqual("completed", module.classify(stream(complete(
            outcome="completed_with_warnings", unreviewedFileCount=0)), 0)["classification"])

    def test_skipped_and_checkpoint_reuse_are_not_clean_analysis(self):
        for event in (complete(status="review_skipped"), complete(message=
                      "No fresh detailed file review was performed in this run. Saved findings follow.")):
            self.assertEqual("skipped", module.classify(stream(event), 0)["classification"])

    def test_auth_completion_is_not_review_completion(self):
        auth = {"type": "complete", "phase": "auth", "status": "authenticated"}
        self.assertEqual("incomplete", module.classify(stream(auth), 0)["classification"])
        self.assertEqual("completed", module.classify(stream(auth, complete()), 0)["classification"])
        self.assertEqual("incomplete", module.classify(stream(
            {"type": "error", "phase": "auth"}, complete()), 0)["classification"])

    def test_errors_exit_status_and_truncation_prevent_completion(self):
        for data, code in ((stream(complete()), 1),
                           (stream({"type": "error"}, complete()), 0),
                           (stream({"type": "heartbeat"}), 0),
                           (stream(complete(), complete()), 0),
                           (stream(complete(), {"type": "finding"}), 0),
                           ('[]\n' + stream(complete()), 0),
                           ('{"type":\n' + stream(complete()), 0),
                           ('', 0)):
            with self.subTest(data=data, code=code):
                self.assertEqual("incomplete", module.classify(data, code)["classification"])

    def test_cli_reads_utf8_and_does_not_echo_findings(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "review.ndjson"
            path.write_text(stream({"type": "finding", "comment": "private code £€"},
                                   complete(findings=1)), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--exit-code", "0"],
                                    capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual("completed", json.loads(result.stdout)["classification"])
            self.assertNotIn("private", result.stdout)
            path.write_text(stream(complete(status="review_skipped")), encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(path), "--exit-code", "0"],
                                    capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(2, result.returncode)
            self.assertEqual("skipped", json.loads(result.stdout)["classification"])


if __name__ == "__main__":
    unittest.main()
