<!-- MEMINIT_PROTOCOL: begin id=agents-md version=1.0 sha256=253a16b17bed3f6c0078437dc88f2b232be7d951de9d2923b1fe219adc1d78ad -->
# Agentic Coding Rules

This repository (**personal-skills**) uses **Meminit DocOps** for governance.

## Using Meminit

Run `meminit` commands to create and manage governed documents:

- `meminit init` — initialize DocOps (run once)
- `meminit capabilities --format json` — discover the command surface
- `meminit context --root . --format json` — discover repo DocOps metadata
- `meminit state next --root . --format json` — select queued work
- `meminit new <TYPE> <TITLE>` — create a new governed document
- `meminit check` — verify compliance
- `meminit doctor` — diagnose repo readiness

Document IDs follow `SKILLS-TYPE-SEQ` (e.g., `SKILLS-ADR-001`).

## Fresh-Agent Loop

A newly instanced agent should work from committed instructions and Meminit
command output:

1. Recognize this repository as Meminit-governed from `AGENTS.md`.
2. Run `meminit capabilities --format json`.
3. Run `meminit context --root . --format json`.
4. Run `meminit state next --root . --format json`; use
   `meminit resolve <DOCUMENT_ID> --root . --format json` for the selected work.
5. Use `meminit index`, `resolve`, `identify`, and `link` to retrieve and cite
   existing information instead of guessing paths.
6. Write back new governed documents with `meminit new <TYPE> <TITLE>
   --format json`; preserve existing `document_id` values when editing.
7. Before declaring done, run `meminit check --root . --format json`,
   `meminit protocol check --root . --format json`, and the repository tests.
   Expect another agent or reviewer to check the work against this loop.

## Rules

- Never modify a `document_id` once set.
- Always use `meminit new` to create governed documents.
- All code changes must include documentation and tests.
- Never commit secrets or PII.
<!-- MEMINIT_PROTOCOL: end id=agents-md -->

# Personal skills repository guidance

This is a private source repository for personal and adapted agent skills. The
installed copies live at each harness's documented discovery path and should be
links to this source, not independent editable copies.

## Authority

Apply instructions in this order:

1. The user's current request.
2. The target repository's `AGENTS.md` and authoritative protocol.
3. A target-specific adapter such as `pepys` or `meminit-docops`.
4. A personal skill in this repository.
5. An unmodified upstream skill.
6. Model defaults.

PEPYS and Meminit should be complementary. If their instructions conflict,
stop and report a protocol defect rather than choosing one silently.

## Change contract

- Treat tests, skill or tooling code, and governed documentation as one atomic
  change.
- Use `meminit new` for new governed documents and preserve document IDs.
- Preserve upstream licence and provenance information for every derivative.
- Keep managed plugin caches read-only. Personal changes belong here.
- Allow only one active provider for a skill name. Give comparison candidates
  a temporary distinct name and disable their implicit invocation.
- Detect upstream updates automatically, but merge them only after review and
  verification.

## Verification

Run before handoff:

```text
python -m unittest discover -s tests -v
python scripts/check_upstreams.py --offline --json
meminit doctor --root . --strict
meminit check --root . --strict
meminit protocol check --root . --format json
```

On Windows, set `PYTHONUTF8=1` for Meminit until its legacy-console Unicode
output defect is fixed. A Windows-only protocol warning about the executable
bit on the generated shell helper is an environment limitation; confirm the
same asset from a native Linux clone before reporting protocol compliance.
