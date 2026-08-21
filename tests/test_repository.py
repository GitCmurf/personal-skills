import json
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "unslop"


def read_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path} has no YAML frontmatter")
    _, block, _ = text.split("---", 2)
    fields: dict[str, str] = {}
    for raw_line in block.strip().splitlines():
        key, separator, value = raw_line.partition(":")
        if not separator:
            raise AssertionError(f"Invalid frontmatter line in {path}: {raw_line}")
        fields[key.strip()] = value.strip().strip('"')
    return fields


class PersonalSkillsRepositoryTests(unittest.TestCase):
    def test_unslop_frontmatter_has_only_supported_fields(self) -> None:
        fields = read_frontmatter(SKILL_DIR / "SKILL.md")
        self.assertEqual({"name", "description"}, set(fields))
        self.assertEqual("unslop", fields["name"])
        self.assertIn("reader-facing prose", fields["description"])
        self.assertIn("Do not use", fields["description"])

    def test_unslop_contract_contains_fidelity_and_authority_guards(self) -> None:
        text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
        required_phrases = (
            "reader cost",
            "fidelity-first",
            "Do not invent",
            "verbatim text",
            "British English",
            "Repository instructions",
            "substantive conversational prose",
        )
        for phrase in required_phrases:
            self.assertIn(phrase, text)

    def test_unslop_ui_metadata_enables_implicit_invocation(self) -> None:
        text = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Unslop"', text)
        self.assertIn("$unslop", text)
        self.assertIn("allow_implicit_invocation: true", text)

    def test_upstream_registry_is_pinned_and_collision_safe(self) -> None:
        registry = json.loads((ROOT / "registry" / "upstreams.json").read_text(encoding="utf-8"))
        self.assertEqual(1, registry["schema_version"])
        self.assertEqual(
            {"pstack", "mattpocock-skills", "superpowers", "impeccable"},
            set(registry["sources"]),
        )
        active_names: list[str] = []
        for skill in registry["skills"].values():
            if skill["activation"] == "active":
                active_names.append(skill["installed_name"])
            baseline = skill.get("upstream_baseline")
            if baseline is not None:
                self.assertRegex(baseline, r"^[0-9a-f]{40}$")
        self.assertEqual(len(active_names), len(set(active_names)))
        self.assertEqual(["unslop"], active_names)

    def test_evaluation_cases_cover_activation_and_protected_material(self) -> None:
        cases = json.loads((ROOT / "tests" / "unslop_cases.json").read_text(encoding="utf-8"))
        categories = {case["category"] for case in cases["cases"]}
        self.assertTrue({"activate", "do-not-activate", "protected-material"} <= categories)
        case_ids = {case["id"] for case in cases["cases"]}
        self.assertTrue(
            {
                "preserve-factual-force",
                "light-touch-short-reply",
                "pepys-reader-facing-prose",
            }
            <= case_ids
        )
        protected = [case for case in cases["cases"] if case["category"] == "protected-material"]
        self.assertTrue(any("verbatim" in case["expect"] for case in protected))
        self.assertTrue(any("code" in case["expect"] for case in protected))

    def test_upstream_checker_runs_offline(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "check_upstreams.py"), "--offline", "--json"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual("offline", payload["mode"])
        self.assertEqual(4, len(payload["sources"]))

    def test_upstream_license_and_attribution_are_preserved(self) -> None:
        text = (SKILL_DIR / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("MIT License", text)
        self.assertIn("Copyright (c) 2026 Lauren Tan", text)


if __name__ == "__main__":
    unittest.main()
