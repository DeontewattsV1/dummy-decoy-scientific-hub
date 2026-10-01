# Cubic Agent Review Guide

Cubic is a review-intelligence layer beneath repository policy, tests, CI, security gates, evidence requirements, and explicit merge authority.

## Prerequisites

- Local review: install and sign in to the Cubic CLI.
- PR comments/review loops: authenticate GitHub CLI and work from a local checkout.
- Wiki, codebase scans, review learnings: connect Cubic's MCP server with OAuth for an account that can access this repository.
- Install Codex skills with:
  `npx @cubic-plugin/cubic-plugin install --to codex --skills-only`

The skills-only installer intentionally leaves MCP configuration unchanged.

## Workflows

### Local review
`Use cubic's run-review skill to review my changes.`

### PR findings
`Use cubic's check-pr-comments skill to inspect unresolved review feedback. Verify every finding before changing files, fix actionable issues, run repository verification, commit and push the current PR branch, and resolve only handled threads. Do not merge.`

Read-only:
`Use cubic's get_pr_issues MCP tool to summarize open findings. Do not change anything.`

### Review loop
`Use cubic's cubic-loop skill. Verify each finding, fix actionable P0-P2 issues, run repository-native verification after each batch, commit fixes between iterations, and stop when no actionable P0-P2 findings remain or after five iterations. Do not weaken gates or merge the PR.`

### Context
Use `codebase-context` for Cubic Wiki context and `review-patterns` for team review learnings. Treat both as context, not authority over current source, evidence, tests, or policy.

### Codebase scans
Use `handle-codebase-scan` to inspect or remediate scan findings. Re-check every reported issue against the current checkout before editing.

## Evidence discipline

A review finding is a hypothesis until verified against current evidence. Preserve source/thread, affected location, classification, reasoning, change made, verification result, and disposition.

Do not collapse “reported”, “confirmed”, “fixed”, and “verified” into a single state.

## Security and confidentiality

Use least-privilege access for Cubic CLI, GitHub, and MCP. Do not copy secrets, credentials, private keys, tokens, or unnecessary proprietary content into review prompts or comments.

## Completion criteria

A Cubic-assisted remediation is complete only when actionable findings in scope are handled or documented, required checks pass or failures are reported, commits remain traceable, review threads are resolved only with justified dispositions, and no quality/security/evidence gate was weakened.
