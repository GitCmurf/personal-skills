---
document_id: SKILLS-ADR-001
type: ADR
title: Review-gated upstream refreshes
status: Draft
version: '0.1'
last_updated: '2026-08-21'
owner: GitCmurf
area: skill-governance
docops_version: '2.0'
template_type: adr-standard
template_version: '2.0'
description: Decision record for maintaining personal adaptations without unmanaged
  drift.
keywords:
- upstream
- updates
---

> **Document ID:** SKILLS-ADR-001
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-08-21
> **Type:** ADR
> **Area:** skill-governance
> **Description:** Decision record for maintaining personal adaptations without unmanaged drift.


# SKILLS-ADR-001: Review-gated upstream refreshes

<!-- MEMINIT_SECTION: title -->

<!-- AGENT: The title should be concise and descriptive of the decision being made. -->

- **Date decided:** 2026-08-21
- **Status:** Draft
- **Deciders:** GitCmurf
- **Consulted:** Codex, through the documented grilling and research
- **Informed:** Agents maintaining or installing personal skills
- **References:** SKILLS-RESEARCH-001, SKILLS-TESTING-001, SKILLS-RUNBOOK-001

## 1. Context & Problem Statement

<!-- MEMINIT_SECTION: context -->

<!-- AGENT: Describe the motivating problem, constraints, and forces. State the scope and what is explicitly out of scope. -->

Personal adaptations must remain recognisably derived from licensed upstreams
without being overwritten by their installers. The repository must also avoid
two active skills with the same name and must work through separate Windows and
WSL checkouts. Public GitHub repositories cannot have private forks in the same
fork network, so “fork everything” is not a sufficient design.

This decision governs acquisition, adaptation and installation. It does not yet
import the planned Matt Pocock, Superpowers or Impeccable skills.

## 2. Decision Drivers

<!-- MEMINIT_SECTION: decision_drivers -->

<!-- AGENT: List the key forces that influence the decision (e.g., latency, cost, safety, operability, compliance, UX, delivery risk). -->

- Preserve the user's voice and reviewed local behaviour.
- Retain licence notices and exact source provenance.
- Detect upstream change without accepting it automatically.
- Keep one active provider for each skill name.
- Avoid editing managed plugin caches.
- Keep Windows and WSL independently usable despite their fragile bridge.
- Keep project adapters thin and subordinate to PEPYS and Meminit authority.

## 3. Options Considered

<!-- MEMINIT_SECTION: options -->

<!-- AGENT: For each option, capture summary, evidence, pros, cons, and risks. Present options fairly. -->

- **Option A: edit managed installations**
  - Pros: immediate and superficially simple.
  - Cons: updates can erase edits; provenance and review history are poor.
  - Evidence: upstream installers recreate or manage their destination folders.
  - Risk: silent loss of personal changes.
- **Option B: copy once and stop tracking upstream**
  - Pros: stable and private.
  - Cons: security, compatibility and quality improvements become invisible.
  - Evidence: no source comparison is retained.
  - Risk: indefinite drift.
- **Option C: private governed repository with pinned upstreams**
  - Pros: reviewable history, automatic change detection and deliberate merges.
  - Cons: each accepted refresh requires human or agent review.
  - Evidence: Git supports exact commit baselines and GitHub supports private
    duplicates outside a public fork network.
  - Risk: update notifications may accumulate if no review cadence is used.

## 4. Decision Outcome

<!-- MEMINIT_SECTION: decision -->

<!-- AGENT: Clearly state the chosen option with rationale tied to decision drivers. Define scope/applicability and status gates. -->

- **Chosen option:** Option C.
- **Why this option:** it preserves both local intent and upstream traceability
  without allowing an updater to rewrite active behaviour.
- **Scope/Applicability:** all skills governed by this repository. Use selective
  vendoring for individual skills and private duplicates where a whole system's
  structure matters.
- **Status gates:** approve after Windows and WSL installations resolve to their
  native checkouts, tests and Meminit checks pass, provenance is complete, and
  PEPYS contains an evidence-backed record.

## 5. Consequences

<!-- MEMINIT_SECTION: consequences -->

<!-- AGENT: Document positive outcomes, negative trade-offs, and any follow-up work needed. -->

- Positive: reviewed personal behaviour is canonical; upstream changes are
  visible; collisions are governed explicitly.
- Negative / trade-offs: an upstream refresh is maintenance work rather than a
  one-command overwrite.
- Follow-up migrations / cleanups: evaluate planned sources individually and
  supersede only the exact installed skills chosen by the owner.

## 6. Implementation Notes

<!-- MEMINIT_SECTION: implementation -->

<!-- AGENT: Include implementation plan, owners, rollout strategy, and monitoring needs. -->

- Plan / milestones: establish repository and `unslop`; install native links;
  then onboard planned sources one at a time.
- Owners: GitCmurf owns decisions; an assigned agent may prepare evidence.
- Backward compatibility / rollout strategy: use a non-implicit candidate name
  where two versions must be compared; activate only one final provider.
- Monitoring: `scripts/check_upstreams.py` compares recorded and remote heads
  without modifying the checkout.

## 7. Validation & Compliance

<!-- MEMINIT_SECTION: validation -->

<!-- AGENT: Specify tests, tooling checks, operational checks, and success metrics. -->

- Tests required: repository structural tests and the synthetic `unslop`
  evaluation contract.
- Tooling checks: official OpenAI skill validation and strict Meminit checks.
- Operational checks: resolve both installation links and run the upstream
  checker in live mode.
- Acceptance criteria: one active provider per name; exact licence and baseline;
  no unattended merge; native Windows and WSL checkouts.

## 8. Alternatives Rejected

<!-- MEMINIT_SECTION: alternatives -->

<!-- AGENT: List rejected options with one-line reason each. -->

- Editing app-managed caches: too easy to overwrite and too hard to audit.
- A one-time untracked copy: hides useful upstream movement.
- Automatic merging: cannot protect local voice or resolve semantic conflicts.
- A public fork: conflicts with the initial private-repository requirement.

## 9. Supersession

<!-- MEMINIT_SECTION: supersession -->

<!-- AGENT: Track what this ADR supersedes and what supersedes it. -->

- Supersedes: none
- Superseded by: SKILLS-ADR-002, for repository visibility only

## 10. Notes for Agents

<!-- MEMINIT_SECTION: agent_notes -->

<!-- AGENT: Include key entities/terms for RAG, code anchors this ADR governs, and known gaps/TODOs. -->

- Key entities/terms for RAG: upstream baseline, personal skill, candidate name,
  installation link, project adapter.
- Code anchors: `registry/upstreams.json`, `scripts/check_upstreams.py`,
  `skills/*`, and `tests/*`.
- Known gaps / TODOs: planned sources are registered but not yet imported.

## 11. Version History

<!-- MEMINIT_SECTION: version_history -->

<!-- AGENT: Track version changes with dates, authors, and change summaries. -->

| Version | Date     | Author    | Changes       |
| ------- | -------- | --------- | ------------- |
| 0.1     | 2026-08-21 | GitCmurf | Initial draft |
