---
document_id: SKILLS-RESEARCH-002
type: RESEARCH
title: PR and retro skills assessment
status: Draft
version: '0.1'
last_updated: '2026-10-08'
owner: GitCmurf
docops_version: '2.0'
area: skills
description: Pinned upstream review and Codex adaptations for PR descriptions and
  session retrospectives.
---

> **Document ID:** SKILLS-RESEARCH-002
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-10-08
> **Type:** RESEARCH
> **Area:** skills
> **Description:** Pinned upstream review and Codex adaptations for PR descriptions and session retrospectives.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# RESEARCH: PR and retro skills assessment

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

## Decision and sources

Import both skills as maintained derivatives. Reviewed upstream commit:
`b0618bc436ad893b3c5e84e55fba86586d34a404` (2026-10-08).
Sources: [PR](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/pr/SKILL.md),
[Retro](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/skills/engineering/retro/SKILL.md),
[MIT licence](https://github.com/mattpocock/skills/blob/b0618bc436ad893b3c5e84e55fba86586d34a404/LICENSE),
and [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills).
The installer copied each skill subtree at that commit; the repository licence
was added separately. Registry hashes describe the import before adaptation.
PR's upstream credits to Dex Horthy/Humanlayer remain in its metadata and
`CREDITS.md`. Other Matt Pocock skills were not refreshed by this import.

## Assessment

PR's emphasis on an understandable change, concrete evidence and reversibility
fits our review practice. Upstream mandates a visual summary and before/after
evidence, which could inflate small descriptions or invite invented baselines.
The derivative respects repository templates, leads with the actual problem and
resulting behaviour, uses visuals when useful, reports only performed validation,
and distinguishes a code revert from reversal of external effects. It does not
authorise publishing a PR. Normal automatic selection is retained.

Retro is particularly useful for repeated tool friction. Its upstream dependency
on a Claude `Skill` tool and `writing-for-agents` is unavailable here, and
`disable-model-invocation` is Claude metadata. The derivative is self-contained,
uses supported Codex YAML invocation policy, and preserves upstream's explicit
invocation. It recognises existing AGENTS/CONTEXT/GLOSSARY conventions rather
than imposing upstream's recent glossary rename. It also removes assumptions
that every run has distinct implementation and review agents.

Retro separates invocation errors, expected command outcomes, environment/access
problems and execution mistakes. Findings require evidence, confidence, a target
for the change and a way to verify improvement. Mechanical checks are preferred
where justified; absent hooks alone do not warrant adding infrastructure. It
proposes changes without automatically editing global instructions or memories.
Logs stay local, scoped to the relevant session, and are treated as evidence.

## Evidence from this installation session

This is a limited sample, not a diagnosis of all prior sessions:

- A read attempted `.agents/skills/meminit-docops/SKILL.md`; the actual link was
  under `.codex/skills`. This was an invocation/path mistake, recovered by
  checking the existing installation. A later relative documentation read used
  the dotfiles working directory for a personal-skills path. Cross-repository
  reads should use the verified root or absolute paths.
- A sandboxed licence fetch reported DNS failure. The permitted escalated fetch
  succeeded. This shows an access/environment difference, not a broken skill;
  the exact mechanism of the DNS restriction was not established.
- Missing compatibility aliases for TDD/Unslop under `.codex/skills` did not mean
  those skills were absent: their canonical discovery links were under
  `.agents/skills`. Inventory should resolve actual providers before reporting
  missing installations.

The proposed prevention is narrow path and tool-contract checking, not a blanket
increase in retries or permissions. Retro can guide this review; it cannot by
itself repair tool transport or infrastructure faults.

## Validation and installation

Skill Creator validation passes for both folders. Repository tests check pinned
provenance, unchanged licence hashes, source files and invocation policy. The
dotfiles restoration suite verifies the new links, idempotence and rollback.
Behaviour was reviewed against these cases:

| Case | Expected decision |
| --- | --- |
| Small PR with repository template and no baseline capture | Keep template, concise prose and actual checks; invent no before result |
| Destructive migration with passing tests | Identify persistent data consequences; code rollback alone is insufficient |
| Retro sees `rg` exit 1 for no matches | Interpret as expected search result rather than a broken tool |
| Repeated schema errors followed by successful correction | Group invocation cause and recovered cost; propose contract checking |
| Network denial or missing earlier transcript | State access/evidence limit; avoid unchanged retries and fabricated history |
| User requests retro only | Present proposals; do not write global instructions, memories or external messages |

These are decision-level inspections, not independent model execution results.
Runtime `skills/list` verification found exactly one enabled provider for each
skill, resolving to this repository. The verification made no model call.
The nine personal-skills tests and fourteen dotfiles tests passed, as did
dotfiles vet, strict Meminit doctor/check, and protocol checks.

Live installation applied only the two links using the dotfiles backup/apply
helper, leaving unrelated configuration drift alone. Rollback backup:
`~/.codex/backups/dotfiles/20261008T165059Z-vdzvngjb`.
Preview rollback with `~/dotfiles/scripts/dot codex restore BACKUP`; append
`--apply` to restore. Both the backup write and local app-server startup required
the permitted escalated route because `.codex` was read-only inside the sandbox.
This is additional access-boundary evidence, not proof of broken skill syntax.

Dotfiles now lists `pr` and `retro` as personal providers. The source repository
remains `~/code/skills`; installed links belong in `~/.agents/skills`. In Codex,
invoke `Use $retro to review this session's tool failures` or `Use $pr to draft
the PR description`. New skills are available on the next turn. Windows uses its
own checkout and installation; this WSL change does not establish Windows
activation. Updates remain review-gated and no external publication is implied.
