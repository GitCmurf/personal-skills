---
document_id: SKILLS-TESTING-001
type: TESTING
title: Unslop evaluation contract
status: Draft
version: '0.1'
last_updated: '2026-08-21'
owner: GitCmurf
docops_version: '2.0'
area: unslop
description: Synthetic evaluation cases and verification commands for unslop.
keywords:
- testing
- unslop
---

> **Document ID:** SKILLS-TESTING-001
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-08-21
> **Type:** TESTING
> **Area:** unslop
> **Description:** Synthetic evaluation cases and verification commands for unslop.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# TESTING: Unslop evaluation contract

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

## Purpose

The evaluation checks activation boundaries and fidelity before judging style.
It uses synthetic prose rather than quick chat messages or existing PEPYS prose;
neither is a reliable sample of the owner's carefully written voice.

## Required cases

`tests/unslop_cases.json` must cover:

- reader-facing prose where `unslop` should act;
- code, commands, quotations, frontmatter, identifiers and evidence that must be
  preserved;
- an explicit audience convention that overrides British English;
- a substantive factual statement whose meaning must not change;
- a short conversational reply where heavy rewriting would cost more than it
  saves; and
- PEPYS prose in which reader-facing explanation may improve but canonical task
  fields and programme terminology remain unchanged.

## Automated verification

Run from the repository root:

```powershell
python -m unittest discover -s tests -v
python scripts/check_upstreams.py --offline --json
uv run --with pyyaml python C:\Users\farme\.codex\skills\.system\skill-creator\scripts\quick_validate.py skills\unslop
$env:PYTHONUTF8 = '1'
meminit doctor --root . --strict
meminit check --root . --strict
```

The structural tests are necessary but not sufficient. Before advancing the
baseline, compare the skill against every synthetic case and record any change in
meaning, protected text, activation or audience convention. A style improvement
does not compensate for a fidelity failure.

## Acceptance rule

Accept only when all automated checks pass, all protected material is unchanged,
no new fact or opinion is invented, and the result is easier for the intended
reader to process. Otherwise keep the current baseline or use a non-implicit
candidate name for further evaluation.
