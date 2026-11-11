---
document_id: SKILLS-RESEARCH-004
type: RESEARCH
title: Consolidate duplicate skills and import grilling and teach
status: Draft
version: '0.2'
last_updated: '2026-11-11'
owner: GitCmurf
docops_version: '2.0'
area: skills
description: One provider per intent for TDD, code review and skill writing, and
  pinned imports of the grilling and teaching skills the owner uses.
---

> **Document ID:** SKILLS-RESEARCH-004
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.2
> **Last Updated:** 2026-11-11
> **Type:** RESEARCH
> **Area:** skills
> **Description:** One provider per intent for TDD, code review and skill writing, and pinned imports of the grilling and teaching skills the owner uses.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# RESEARCH: Consolidate duplicate skills and import grilling and teach

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

Claude Code sessions were loading three or four skills for each of three
intents (TDD, code review, writing skills), from this repository, the synced
`mattpocock-skills` plugin and the now-disabled `superpowers` plugin. Which one
ran depended on wording. The owner wants a single skill per intent, and wants to
keep `teach` and `grill-with-docs` once the plugin is switched off.

All imports come from a clone of `mattpocock/skills` at
`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` (2026-10-31, MIT). The registry
records each skill's hashes before adaptation. The source's `tracked_head` is
unchanged: it marks the upstream state that has been reviewed for update
detection, not the newest import.

## Decisions

- **TDD stays `tdd`, unchanged.** The current upstream skill was compared with
  the personal one. Its additions (independent expected values, vertical slices,
  glossary and ADR awareness) are already covered. Upstream now requires the
  user to confirm each test seam before any test; the personal skill proceeds
  when the request and repository already establish the boundaries. That
  difference is deliberate, so nothing was merged.
- **Code review merges into `code-review`.** The upstream two-axis review
  (repository standards and the originating spec, as parallel sub-agents) is
  added as `references/two-axis-review.md` with its MIT licence beside it. The
  skill now starts with that local review and adds CodeRabbit when asked, or
  when a change is worth a rate-limited slot. Adaptations: the tracker-setup
  line was removed, a missing fixed point defaults to the default-branch
  merge-base, and issues are fetched with the repository's issue tool. The
  derivation is recorded under `additional_derivations` in the registry.
- **Skill writing moves to `writing-for-agents`.** Upstream has replaced
  `write-a-skill` with this reference. It is imported unchanged, and the
  installed `write-a-skill` is retired. The built-in Claude `skill-creator`
  remains: it covers packaging and evaluation and cannot be switched off here.
- **`grill-with-docs` is imported with the two skills it composes.** Upstream
  turned it into a wrapper that invokes `grilling` and `domain-modeling`, so all
  three are imported. The wrapper's "call the Skill tool" line was reworded to
  name both the Claude Code and the Codex invocation. `teach` is imported
  unchanged.
- **Codex metadata.** `grilling`, `domain-modeling` and `writing-for-agents`
  gained an explicit `allow_implicit_invocation: true`, matching their
  model-invoked frontmatter and the repository's metadata convention.
- **`diagnosing-bugs` is imported (v0.2, 2026-11-11).** With both plugins off,
  no skill covered bug diagnosis, so the owner asked for it. It is imported
  unchanged from the same baseline, including its human-in-the-loop script
  template, and gains the same explicit Codex invocation policy. It names no
  other skill.

## Validation and limits

Repository tests assert the active-provider set, the licence hash and invocation
policy of every pinned import, that `code-review` points at the two-axis
reference and carries its licence, and that `grill-with-docs` composes active
skills. `diagnosing-bugs` is covered by the same pinned-import checks. No
behavioural evaluation of the merged review was run. Switching off the synced
plugin is an owner action on claude.ai or through `/plugin`; until
then, the plugin's copies remain loaded alongside these.
