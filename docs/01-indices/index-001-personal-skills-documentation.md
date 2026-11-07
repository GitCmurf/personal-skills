---
document_id: SKILLS-INDEX-001
type: INDEX
title: Personal skills documentation
status: Draft
version: '0.1'
last_updated: '2026-10-08'
owner: GitCmurf
docops_version: '2.0'
area: repository
description: Entry point for governed personal-skills documentation.
keywords:
- index
---

> **Document ID:** SKILLS-INDEX-001
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-10-08
> **Type:** INDEX
> **Area:** repository
> **Description:** Entry point for governed personal-skills documentation.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# INDEX: Personal skills documentation

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

This public repository is the canonical home for the owner's personal and
adapted agent skills. `skills/` contains active source; standard discovery
locations link to it. `registry/upstreams.json` records licensed origins and
reviewed baselines.

## Start here

- [Upstream skill sources](../10-prd/research-001-upstream-skill-sources.md)
  records the primary-source research and acquisition implications.
- [Review-gated upstream refreshes](../45-adr/adr-001-review-gated-upstream-refreshes.md)
  is the governing architecture decision.
- [Unslop evaluation contract](../55-testing/testing-001-unslop-evaluation-contract.md)
  defines the fidelity and activation tests.
- [Install personal skills on Windows and WSL](../60-runbooks/runbook-001-install-personal-skills-on-windows-and-wsl.md)
  gives the operational procedure and known Meminit limitations.
- [Personal skills glossary](../70-devex/ref-001-personal-skills-glossary.md)
  defines repository terms.
- [PR and Retro assessment](../10-prd/research-002-pr-and-retro-skills-assessment.md)
  records the pinned imports, Codex adaptations and tool-failure review criteria.

- [CodeRabbit 0.9 skill refresh](../10-prd/research-003-coderabbit-09-skill-refresh.md)
  records CLI compatibility, selective upstream adaptations and stream validation.
- [Publish the personal skills repository](../45-adr/adr-002-publish-the-personal-skills-repository.md)
  records the move to public visibility and the no-PII rule.

## Current scope

Active personal providers are `unslop`, `tdd`, `code-review`, `pr` and `retro`.
Retro preserves explicit invocation; PR can be selected when drafting a PR body.
Superpowers and Impeccable remain planned sources. The registry is authoritative
for provider provenance and activation.
