---
document_id: SKILLS-RESEARCH-003
type: RESEARCH
title: CodeRabbit 0.9 skill refresh
status: Draft
version: '0.2'
last_updated: '2026-11-07'
owner: GitCmurf
docops_version: '2.0'
area: skills
description: Compatibility assessment and verification of the CodeRabbit 0.9 personal
  skill.
---

> **Document ID:** SKILLS-RESEARCH-003
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.2
> **Last Updated:** 2026-11-07
> **Type:** RESEARCH
> **Area:** skills
> **Description:** Compatibility assessment and verification of the CodeRabbit 0.9 personal skill.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# RESEARCH: CodeRabbit 0.9 skill refresh

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

The existing skill remains appropriate as the default CodeRabbit review provider.
Core scope flags work in the installed CLI 0.9.0, but its 0.8.2-era instructions
needed correction. The canonical source and both installed links were checked;
links resolve to `skills/code-review` in this repository.

## Evidence and upstream decision

The installed `coderabbit --version`, root help, review help, auth-status help
and findings help were inspected. The [official command reference](https://docs.coderabbit.ai/cli/reference)
still identifies its generated version as 0.8.2. The [output contract](https://docs.coderabbit.ai/cli/agent-mode)
and [local-review guide](https://docs.coderabbit.ai/cli/index) establish stream
completion, incomplete coverage, checkpoint behaviour and selected-file rules.

Public upstream `coderabbitai/skills` was inspected at
`928c3b61f71b578b1bcfbacc289f1446244dd9dd`. Its review entrypoint and references
provide useful recovery, severity and saved-result guidance. However, upstream
also describes `--light`, absent from the installed review help, and says not
to promise `usage --agent`, which is supported by this binary. Wholesale copying
would reproduce version mismatches. We selectively adapted the useful behaviour
and recorded the reviewed commit and file hashes separately from the original
unknown-baseline import. The original MIT licence and snapshot hashes remain.

## Changes and rationale

- Preserve native severities instead of inventing Critical/Warning/Info groups.
- Permit directory scopes inside a worktree; no independent `.git` is required.
- Distinguish NDJSON liveness, auth completion, analysis completion, skipped
  checkpoints, failed outcomes and unreviewed files. A `review_completed` event
  may still describe failure; process exit and coverage also matter.
- Add a local stream checker to make these distinctions repeatable without
  echoing source or prompts. It returns exit 0 for completed analysis and exit 2
  for skipped or incomplete results; its finding count is not a correctness
  assessment. Findings still need substantive review and local verification.
- Preserve selected scope and repository authorization; inspect unstaged and
  included untracked content as well as staged changes before disclosure.
- Use supported elevation for restricted network/storage/socket operations;
  distinguish sandbox access errors from host logout. Stop unchanged retries,
  honour rate limits and avoid automatic credit spending.
- Use one analysis and one verification pass by default, allowing further work
  for material unresolved issues rather than an unlimited until-clean loop.
- Explain stored results, stale findings and PR prompts in a conditional
  reference. New cloud-coding, handoff and publication capabilities are separate
  actions, not part of an ordinary review.

## Validation and limits

Unit tests exercise completed reviews, findings, warnings with full coverage,
failed and unknown outcomes, uncovered files, mismatched counts, auth-only
completion, skipped analysis, checkpoint reuse, error events, duplicate/truncated
streams, nonzero process exit and UTF-8 handling. A subprocess test verifies the
helper exit codes and that its output omits private finding text. Repository
provenance and licence checks remain required, as do Skill Creator validation,
offline upstream checks and strict Meminit doctor/check/protocol checks.

Decision inspection confirmed that a generic private-repository review with no
CodeRabbit disclosure approval continues locally; existing target authorization
permits the requested run without asking again. A heartbeat or skipped review
cannot justify saying the code is clean. Saved findings cannot establish current
coverage. These inspections are not independent model evaluations.

No live code was uploaded, no paid credit option was exercised, and no account,
organization, region or CodeRabbit configuration was changed. This establishes
local CLI compatibility and helper behaviour, not a new end-to-end cloud review.
The installed discovery links activate source changes without copying or running
`coderabbit skills`; restart or reload a cached skill context if necessary.

## Amendment 2026-11-07: free-tier review allowance

On the free tier, local CLI reviews and the GitHub PR bot draw on one small,
rate-limited allowance. Observed on 2026-10-29, both reported "review limit
reached" against the same dashboard, and the bot's footer stated about one
included review per hour. Local runs before every push starved the PR bot.

The owner's decision is that the CLI stays useful but is used judiciously. The
skill now says to run a CLI review when its feedback is worth a slot (a requested
review, or the riskiest change in a task), not by reflex before every push, and
to report a review limit and continue locally rather than retry. A repository
test asserts this guidance is present.
