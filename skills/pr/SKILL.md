---
name: pr
description: "Draft or revise a pull request description with clear change, validation evidence, and merge risk. Use when writing a PR body."
metadata:
  credits:
    skill: show-me
    author: Dex Horthy
    organisation: Humanlayer
    url: "https://github.com/humanlayer/skills/blob/main/plugins/show-me/skills/show-me/SKILL.md"
---

# PR descriptions

Write for a reviewer who has not seen the conversation. Follow the repository's
PR template and the user's format first. Use its established domain language
from `GLOSSARY.md`, `CONTEXT.md`, or other authoritative docs; do not require a
renaming or setup step. This skill shapes a description; it does not authorise
pushing, opening, merging, or posting anything.

Inspect the actual change and available validation before drafting. Use the
issue, spec, or user request to explain the problem; use the diff to verify what
was implemented. If scope changed, describe the final implementation. Do not
present a planned feature as shipped or review as completed without evidence.

Without a repository template, use these sections, scaled to the change:

## Summary

Lead with the concrete problem and resulting behaviour. A trigger and before/
after example often makes this clear in one or two sentences.

Choose the smallest visual when it helps: pseudocode for logic, a call tree for
control flow, a component tree for UI boundaries, a shallow file tree for
responsibilities, Mermaid for interactions, or a diff sketch for the changed
shape. Keep only the calls, files, states and boundaries the reviewer needs.
Place a visual next to the short explanation it supports. A simple edit can be
clearer in prose; do not force a diagram into every PR.

For example:

```text
save(content)
  unchanged -> return cached result
  changed   -> persist content, invalidate cache
```

Label sketches as illustrative; do not imply that pseudocode is executed code.
Preserve the upstream visual guidance attribution in [CREDITS.md](CREDITS.md).

## Evidence

Give inspectable evidence, preferably a before/after pair when captured:
screenshots for visual behaviour, or the exact regression test or observed
output for logic. State the command, result, and what it demonstrates. Test
pseudocode can explain a case but cannot establish that it ran.

Report only checks actually performed. If a before capture is unavailable, say
so briefly when relevant and give the available evidence. If a check failed or
was blocked, state that limitation. Do not invent a failing baseline, screenshot,
test result, or claim that passing tests prove every path safe.

## Merge risk

Describe reversibility and affected consumers or runtime paths. Distinguish a
cheap rollback (a two-way door) from destructive migrations, lost data, public
API removals, or other hard-to-reverse consequences (a one-way door). A code
revert does not necessarily reverse an external effect.

Name the blast radius concretely rather than forcing it into one word. Include
rollout or recovery detail only when it helps assess the change. For a small
local change, a short risk statement is enough; do not create a new approval
process from this template.
