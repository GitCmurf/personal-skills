---
name: tdd
description: Build features or fix bugs test-first using red-green-refactor. Use when the user requests TDD, test-first development, or integration tests.
---

# Test-driven development

Use small red-green-refactor cycles to deliver the requested behaviour. Tests
should exercise meaningful public boundaries and survive internal refactoring.
Explicit user instructions and existing project conventions take precedence.

## Establish the scope

Use the request, existing tests, and relevant code to identify the expected
behaviour and the public interface under test. Consult the project's glossary
and architectural decisions when they affect the change; preserve its existing
file names and conventions.

Briefly state the behaviours and boundaries you will test. When the request and
repository already establish them, proceed without asking for another approval.
Ask a focused question only when unresolved behaviour or an interface choice
would materially change the outcome. Continue independent work while waiting.
Respect any explicit requirement to approve a plan before implementation.

Prioritise the reported failure, critical paths, and relevant edge cases. Avoid
unrelated architecture work and exhaustive testing of low-risk details. Read
[interface-design.md](interface-design.md) or [deep-modules.md](deep-modules.md)
when the task actually requires designing a new boundary.

## Work in vertical slices

1. Write one test for an agreed or clearly specified behaviour. Verify it fails
   for the expected missing behaviour or defect, rather than a setup error.
2. Implement the smallest coherent change that makes it pass.
3. Repeat for the remaining required behaviours. Use each result to refine the
   next slice; do not write a speculative batch of tests before implementation.
4. Refactor when green if it improves the changed code. Keep the relevant tests
   passing and stay within the requested scope. See [refactoring.md](refactoring.md)
   when substantial refactoring is warranted.

## Make the tests informative

- Exercise actual behaviour through the appropriate public interface. Prefer
  integration tests when the risk lies in interactions between components.
- Choose expected values independently of the implementation: a specification,
  known example, or independently worked result. Do not recompute the same
  algorithm inside the assertion or merely match source text.
- Avoid coupling tests to private methods, incidental call order, or internal
  structure. Mock external boundaries only when doing so preserves the behaviour
  under test. See [tests.md](tests.md) and [mocking.md](mocking.md) as needed.
- Make regressions fail observably. A passing test alone does not establish that
  it would detect the original defect.

## Complete the work

Continue through the requested behaviour, relevant regression checks, and
required repository checks. Once they pass, expand testing only when remaining
risk or new evidence warrants it. Report what works, what was verified, and any
unresolved limitation. Do not stop after the first passing slice when more of
the authorised task remains.
