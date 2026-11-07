---
document_id: SKILLS-ADR-002
type: ADR
title: Publish the personal skills repository
status: Draft
version: '0.1'
last_updated: '2026-11-07'
owner: GitCmurf
docops_version: '2.0'
template_type: adr-standard
template_version: '2.0'
---

> **Document ID:** SKILLS-ADR-002
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-11-07
> **Type:** ADR


# SKILLS-ADR-002: Publish the personal skills repository

<!-- MEMINIT_SECTION: title -->

<!-- AGENT: The title should be concise and descriptive of the decision being made. -->

- **Date decided:** 2026-11-07
- **Status:** Draft
- **Deciders:** GitCmurf (owner)
- **Consulted:** Claude Code session preparing the change
- **Informed:** Agents working in this repository, through this ADR and `AGENTS.md`
- **References:** SKILLS-ADR-001 (private governed repository with pinned upstreams)

## 1. Context & Problem Statement

<!-- MEMINIT_SECTION: context -->

<!-- AGENT: Describe the motivating problem, constraints, and forces. State the scope and what is explicitly out of scope. -->

SKILLS-ADR-001 chose a private governed repository with pinned upstreams.
The owner now wants the repository public, on one condition: it must hold no
personally identifying information (PII). A scan of the full history before
publication found the owner's real name in document metadata and prose, and
the owner's local user name in example paths. It found no credentials, tokens,
keys or personal email addresses: commits use a GitHub no-reply address.

Scope: repository visibility and the PII rule. Out of scope: the upstream
pinning, review-gated refresh and one-active-provider rules in SKILLS-ADR-001,
which still apply unchanged.

## 2. Decision Drivers

<!-- MEMINIT_SECTION: decision_drivers -->

<!-- AGENT: List the key forces that influence the decision (e.g., latency, cost, safety, operability, compliance, UX, delivery risk). -->

- No PII may be published, in current files or in history.
- Vendored upstream skills must keep their licences and attribution, which
  their MIT and Apache-2.0 licences permit publishing.
- Naming the owner's other projects (for example PEPYS) is acceptable to the
  owner.
- Installed skill links point at this checkout, so the rewrite must keep paths
  stable.

## 3. Options Considered

<!-- MEMINIT_SECTION: options -->

<!-- AGENT: For each option, capture summary, evidence, pros, cons, and risks. Present options fairly. -->

- **Option A:** Stay private.
  - Pros: no disclosure risk.
  - Cons: does not meet the owner's request.
  - Evidence / benchmarks: n/a.
  - Risks / unknowns: none.
- **Option B:** Publish after scrubbing current files only.
  - Pros: no history rewrite.
  - Cons: the name stays readable in earlier commits.
  - Evidence / benchmarks: the pre-publication scan found the name in 34 history lines.
  - Risks / unknowns: fails the no-PII condition.
- **Option C:** Rewrite history to remove PII, then publish.
  - Pros: meets the no-PII condition across all commits.
  - Cons: every commit ID changes and the remote needs a force-push.
  - Evidence / benchmarks: single-owner repository with no forks, pull requests or other clones in use.
  - Risks / unknowns: GitHub may keep pre-rewrite commits reachable by exact ID; those IDs were never published.

## 4. Decision Outcome

<!-- MEMINIT_SECTION: decision -->

<!-- AGENT: Clearly state the chosen option with rationale tied to decision drivers. Define scope/applicability and status gates. -->

- **Chosen option:** Option C.
- **Why this option:** it is the only option that publishes without PII.
- **Scope/Applicability:** the whole repository. From now on, refer to the
  owner as `GitCmurf` or "the owner", and write home paths as `~/` or
  `%USERPROFILE%\`.
- **Status gates:** the history scan finds no PII, and the repository
  verification block in `AGENTS.md` passes, before visibility changes.

## 5. Consequences

<!-- MEMINIT_SECTION: consequences -->

<!-- AGENT: Document positive outcomes, negative trade-offs, and any follow-up work needed. -->

- Positive: the skills are shareable, and changes stay reviewable in public.
- Negative / trade-offs: commit IDs changed on 2026-11-07, and the
  "private duplicate" strategy in SKILLS-ADR-001 now produces public copies.
  Publishing them is allowed only when the upstream licence permits it.
- Follow-up migrations / cleanups: scan new content for PII before each push.

## 6. Implementation Notes

<!-- MEMINIT_SECTION: implementation -->

<!-- AGENT: Include implementation plan, owners, rollout strategy, and monitoring needs. -->

- Plan / milestones: back up the repository as a git bundle, rewrite with
  `git filter-repo --replace-text`, update wording that calls the repository
  private, verify, force-push, then change visibility.
- Owners: GitCmurf.
- Backward compatibility / rollout strategy: the local checkout was rewritten
  in place, so installed skill links keep working. Any other clone must be
  re-cloned.
- Telemetry / monitoring to add: none.

## 7. Validation & Compliance

<!-- MEMINIT_SECTION: validation -->

<!-- AGENT: Specify tests, tooling checks, operational checks, and success metrics. -->

- Tests required (unit/integration/e2e): the existing repository tests.
- Tooling checks (lint/format/static analysis): `gitleaks` over full history,
  plus a full-history search for the owner's name and local user name.
- Operational checks (dashboards/alerts/runbooks): the verification block in `AGENTS.md`.
- Success metrics or acceptance criteria: zero PII matches in `git log -p --all`.

## 8. Alternatives Rejected

<!-- MEMINIT_SECTION: alternatives -->

<!-- AGENT: List rejected options with one-line reason each. -->

- Option A: does not meet the owner's request.
- Option B: leaves PII in history.

## 9. Supersession

<!-- MEMINIT_SECTION: supersession -->

<!-- AGENT: Track what this ADR supersedes and what supersedes it. -->

- Supersedes: SKILLS-ADR-001, for repository visibility only.
- Superseded by: none

## 10. Notes for Agents

<!-- MEMINIT_SECTION: agent_notes -->

<!-- AGENT: Include key entities/terms for RAG, code anchors this ADR governs, and known gaps/TODOs. -->

- Key entities/terms for RAG: public repository, PII, history rewrite, GitCmurf.
- Code anchors (paths, modules, APIs) this ADR governs: the whole repository; `AGENTS.md`.
- Known gaps / TODOs: the repository has no top-level licence for its own
  content. Vendored skills keep their upstream licences.

## 11. Version History

<!-- MEMINIT_SECTION: version_history -->

<!-- AGENT: Track version changes with dates, authors, and change summaries. -->

| Version | Date     | Author    | Changes       |
| ------- | -------- | --------- | ------------- |
| 0.1     | 2026-11-07 | GitCmurf | Initial draft |
