---
document_id: SKILLS-RESEARCH-001
type: RESEARCH
title: Upstream skill sources
status: Draft
version: '0.1'
last_updated: '2026-08-21'
owner: GitCmurf
docops_version: '2.0'
area: skill-governance
description: Primary-source findings for upstream skill acquisition and maintenance.
keywords:
- upstream
- licensing
---

> **Document ID:** SKILLS-RESEARCH-001
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.1
> **Last Updated:** 2026-08-21
> **Type:** RESEARCH
> **Area:** skill-governance
> **Description:** Primary-source findings for upstream skill acquisition and maintenance.

<!-- MEMINIT_SECTION: title -->
<!-- AGENT: State the document objective clearly. -->

# RESEARCH: Upstream skill sources

<!-- MEMINIT_SECTION: content -->
<!-- AGENT: Fill this section with the document-specific content. -->

## Content

## Question

How should personally adapted skills retain a reviewable relationship with their
upstreams while remaining private, collision-safe and usable in both Windows and
WSL?

## Primary-source findings

- OpenAI documents `$HOME/.agents/skills` as the user-level location shared by
  Codex desktop, CLI and IDE integrations. It also documents symlinked skill
  folders. ChatGPT web and mobile distribution is a separate plugin concern.
  Source: [Build skills](https://learn.chatgpt.com/docs/build-skills).
- GitHub states that all repositories in a public repository's fork network are
  public. A private personal repository therefore cannot be an ordinary GitHub
  fork of these public projects. Source: [About permissions and visibility of
  forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks).
- GitHub documents repository duplication as a way to maintain a separate copy.
  That supports private duplicates for whole-repository imports, with the public
  source recorded separately as an upstream. Source: [Duplicating a
  repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository).
- The copied `unslop` skill comes from `pstack/skills/unslop` in Cursor's plugin
  repository. The plugin is MIT-licensed; its notice is preserved in
  `skills/unslop/LICENSE`. Sources: [pstack source](https://github.com/cursor/plugins/tree/main/pstack),
  [pstack licence](https://github.com/cursor/plugins/blob/main/pstack/LICENSE).
- Matt Pocock's skills are distributed from a standalone MIT repository.
  Superpowers is a multi-harness MIT repository. Impeccable is the remembered
  name of the frontend-design system and is Apache-2.0 licensed. Sources:
  [mattpocock/skills](https://github.com/mattpocock/skills),
  [obra/superpowers](https://github.com/obra/superpowers), and
  [pbakaus/impeccable](https://github.com/pbakaus/impeccable).

## Repository implications

Use selective vendoring when only a small skill subtree is wanted. Use a private
duplicate with a recorded public upstream for a system whose repository structure
is material. In either case, pin the reviewed upstream commit in
`registry/upstreams.json`. Detection of a newer head is automatic and read-only;
incorporation is manual and must include attribution, tests, code and governed
documentation.

The initial registry activates only the adapted `unslop`. The other sources are
registered as planned work, not installed or silently superseded.
