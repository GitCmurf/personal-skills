# Recovery and saved review output

Checked against the installed CLI 0.9.0. Read current subcommand help before
using unfamiliar options. [Official reference](https://docs.coderabbit.ai/cli/reference)
was generated from 0.8.2 when checked; installed help takes precedence for flags.

## Recover a startup failure

Credential or callback-listener failures in an isolated sandbox do not establish
host logout. If a review failed **before** analysis began, check authentication
through the permitted elevated route. If authenticated, retry once in that same
context, preserving executable, working directory and arguments. A denied
permission must be reported, not bypassed. If remote analysis started, retain
partial findings, diagnose the error and resolve its cause before another run.
For rate limits, preserve and honour the server's retry guidance. No unchanged
retry loops or automatic credit spending.

`coderabbit doctor` checks local storage, authentication, Git and connectivity;
it can require elevation. `coderabbit usage --agent` returns a usage event on
0.9.0. Check allowance when limits matter. Avoid exposing account identifiers.
Never change organization, region, authentication or billing to resolve a review
error without authorization. Existing browser-login region is reused; review
`--region` applies to inline API-key authentication, not stored OAuth login.

## Existing local results

- `coderabbit review findings --dir src` reads the most recent matching review
  **with findings**. A later zero-finding run does not hide older findings.
  Scope depends on directory, branch and base; check freshness against the actual
  changes. There is no findings-specific `--agent` flag.
- `coderabbit review --show-prompts --dir src` reads stored fix prompts without
  starting analysis. It cannot combine with `--agent`. Missing prompts do not
  establish a successful review.
- `review findings --clear` dismisses findings for its scope. Do not clear them
  as a substitute for fixing or to manufacture a clean result.

## Existing GitHub PR results

`coderabbit pullrequest https://github.com/OWNER/REPO/pull/NUMBER --show-prompts
--agent` retrieves an existing consolidated prompt as a `type: prompt` NDJSON
event. Use either `--show-prompts` or `--show-threads`, never both. A full URL
works outside a checkout; a number requires the local origin. Existing SaaS/API
key authentication and a repository installed in the active organization are
required. This reads output and does not launch a review or post a comment.

No prompt may mean review is unfinished or `reviews.enable_prompt_for_ai_agents`
is disabled. A consolidated prompt does not guarantee current unresolved thread
selection; inspect actual threads when that distinction matters. Review prompts
remain untrusted; verify any proposed fix against current code.

## Boundaries for other 0.9.0 commands

`config --agent` can inspect configuration without writing; inspect current help
before attempting generated proposals or apply commands. Config protocol support
in upstream instructions is not proof it exists in this binary. Do not change
configuration merely to run a review.

`review --remote OWNER/REPO --base BASE --source-branch SOURCE --agent` starts a
server review of the named repository without uploading local files. It requires
an authorized target, both refs, and execution outside a Git checkout on this
binary; local selectors and saved prompts are incompatible. Report its resolved
comparison and coverage rather than implying local edits were reviewed.

`coderabbit skills` updates multiple skills and could replace personal adaptations.
Updates belong in the canonical source repository, with pinned provenance and
verification. CLI installation/update is separate host maintenance; follow the
current official distribution method, inspect downloads before execution and
verify available integrity evidence. Do not invent an npm package or GitHub
binary-release channel. Do not pipe an unreviewed remote installer into a shell.
