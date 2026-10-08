---
document_id: SKILLS-RUNBOOK-001
type: RUNBOOK
title: Install personal skills on Windows and WSL
status: Draft
version: '0.3'
last_updated: '2026-10-08'
owner: GitCmurf
area: installation
docops_version: '2.0'
template_type: runbook-standard
template_version: '2.0'
description: Canonical installation and update procedure for Windows and WSL.
keywords:
- windows
- wsl
- skills
---

> **Document ID:** SKILLS-RUNBOOK-001
> **Owner:** GitCmurf
> **Status:** Draft
> **Version:** 0.3
> **Last Updated:** 2026-10-08
> **Type:** RUNBOOK
> **Area:** installation
> **Description:** Canonical installation and update procedure for Windows and WSL.


<!-- MEMINIT_SECTION: title -->
<!-- AGENT: The title should be concise and descriptive of the runbook procedure. -->

# RUNBOOK: Install personal skills on Windows and WSL

<!-- MEMINIT_SECTION: executive_summary -->
<!-- AGENT: Write a 2-3 sentence overview of what procedure this runbook governs and when to run it. -->

## 0. Overview

This procedure installs the private canonical repository for Codex desktop and
CLI use. Windows and Ubuntu use separate native checkouts; the standard discovery
folders contain links, not editable copies.

<!-- MEMINIT_SECTION: context -->
<!-- AGENT: List prerequisites, environment setup, and tools needed. -->

## 1. Prerequisites and Context

- Git and Python are available in both environments.
- Windows uses GitHub Credential Manager over HTTPS.
- WSL retains SSH and uses a persistent user `ssh-agent`; it is not switched to
  HTTPS for routine work.
- The private remote is `GitCmurf/personal-skills`.
- OpenAI's documented user-level discovery location is `$HOME/.agents/skills`.
- Managed plugin caches under `.codex/plugins/cache` are not edited.

<!-- MEMINIT_SECTION: decision -->
<!-- AGENT: List the operational steps or procedures to execute. -->

## 2. Procedure Steps

1. Clone the repository to `%USERPROFILE%\code\skills` on Windows using HTTPS.
2. Link each active skill into `C:\Users\farme\.agents\skills`. For `unslop`,
   create a directory junction whose target is
   `%USERPROFILE%\code\skills\skills\unslop`.
3. Clone the same repository to `~/code/skills` in Ubuntu. An HTTPS clone
   may be used for the first bootstrap; set its final `origin` to
   `git@github.com:GitCmurf/personal-skills.git`.
4. Link `~/.agents/skills/unslop` to
   `~/code/skills/skills/unslop`.
5. Configure the WSL user agent at
   `~/.config/systemd/user/ssh-agent.service`, exporting
   `SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/ssh-agent.socket` from Bash. In
   `~/.ssh/config`, give `github.com` the existing `id_ed25519` identity and set
   `AddKeysToAgent yes`. Enable the user service.
6. On first interactive SSH use, enter the key passphrase once. The key remains
   in that user agent for its lifetime. Do not remove the passphrase.
7. For an upstream refresh, run the read-only checker, review the upstream diff,
   update tests, code, governed docs, licence material and the recorded baseline
   together, then commit. Never edit an installed link or managed cache directly.

<!-- MEMINIT_SECTION: validation -->
<!-- AGENT: Specify how to verify that the runbook was executed successfully. -->

## 3. Verification

From each checkout, run the commands in SKILLS-TESTING-001. Then verify that:

- the `unslop` installation path resolves to that environment's native checkout;
- `origin` is HTTPS on Windows and SSH in WSL;
- `ssh-add -l` in WSL reports the existing key after its first unlock;
- no second active skill named `unslop` is present; and
- Codex sees the skill after its next skill-discovery refresh or restart.

<!-- MEMINIT_SECTION: risk_management -->
<!-- AGENT: Detail troubleshooting steps, rollbacks, and recovery methods. -->

## 4. Troubleshooting and Recovery

- If SSH asks on every operation, check that `SSH_AUTH_SOCK` names the running
  systemd user service's socket and that `ssh-add -l` can reach it. A passphrase
  prompt after a reboot or agent restart is expected; a prompt for every Git
  operation is not.
- If Windows cannot print Meminit's status symbols, set `PYTHONUTF8=1`. Version
  0.2.0 currently fails under the default Windows code page during `meminit init`.
- The present Windows `meminit.exe` imports its Python package from the Ubuntu
  development checkout through `\\wsl$`. Treat this as a Meminit deployment
  defect: Windows is not independent while that remains true.
- Ubuntu currently adds `~/.local/bin` to `PATH` more than once. This is harmless
  but should be cleaned during the Meminit deployment work.
- `docker-desktop` does not contain Meminit. It is an appliance distro, not a
  personal development shell; do not modify it merely to satisfy a literal
  “all distributions” check.
- On native Windows, `meminit protocol check` may report the generated shell
  helper as mode `0666` rather than `0755`. Preserve the executable bit in Git;
  validate the mode-sensitive protocol from WSL.
- If PEPYS and Meminit instructions contradict each other, stop and record a
  defect. Do not silently choose one.

<!-- MEMINIT_SECTION: version_history -->
<!-- AGENT: Track version changes with dates, authors, and change summaries. -->

## 5. Version History

| Version | Date     | Author    | Changes       |
| ------- | -------- | --------- | ------------- |
| 0.1     | 2026-08-21 | GitCmurf | Initial draft |
| 0.2     | 2026-10-03 | GitCmurf | Codex restoration and maintained TDD/CodeRabbit providers |
| 0.3     | 2026-10-08 | GitCmurf | Add pinned PR and Retro derivatives and their invocation guidance |

## Codex restoration from dotfiles

The WSL dotfiles checkout at `~/dotfiles` owns Codex preference restoration and
skill linking. Run `~/dotfiles/scripts/dot codex preview`, then `apply` to
recreate the selected configuration and links. Its backups can be previewed
and restored with `scripts/dot codex restore BACKUP` and the `--apply` flag.
See `~/dotfiles/docs/codex.md` for the full command contract.

The active personal providers are `unslop`, `tdd`, `code-review`, `pr`, and `retro`. TDD retains
red-green-refactor and meaningful behavioural tests while honouring already
authorised work. CodeRabbit commands match the installed 0.8.2 CLI. These are
maintained derivatives, not exact copies of the current upstream heads. Their
licences, imported file hashes and installer provenance are recorded in
`registry/upstreams.json`. Review upstream updates before incorporating them;
do not bulk-update these installed links with a third-party skill installer.

PR and Retro are pinned Codex adaptations assessed in SKILLS-RESEARCH-002.
Use `$pr` to draft a PR body, or `$retro` to review a session's friction and
propose improvements. Retro retains explicit invocation and does not write
global instructions or memory automatically. Dotfiles restores both links into
`~/.agents/skills`; verify their targets and discovery on the next turn.

PEPYS and Meminit remain owned by their respective source repositories. The
dotfiles workflow links them rather than vendoring or editing their protocols.
