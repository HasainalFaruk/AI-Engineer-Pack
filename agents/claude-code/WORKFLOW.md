# Claude Code Workflow

## 1. Define the task
Write the goal, acceptance criteria, files or systems in scope, and actions that require approval.

## 2. Configure the environment
Install or enable the tool, connect required services, configure repository instructions, and verify permissions.

## 3. Start with read-only work
Ask the agent to inspect, summarize, or plan before granting write access.

## 4. Execute scoped work
Start in a clean worktree, ask for a plan, let Claude inspect, approve scoped edits, run tests, review diffs, then commit or open PR after human approval.

## 5. Verify behavior
Run project test suites, lint, type checks, and task-specific smoke tests; verify that hooks and CI reproduce local results..

## 6. Review and deploy
Use CI/CD integrations for review and automation, never deploy directly without human approval, and use scheduled tasks only with scoped permissions..

## 7. Improve from failures
Review failed runs, prompts, traces, logs, and human corrections before increasing autonomy.
