---
name: help
description: Explain cleanResearch and guide a beginner to the right skill or action. Use when the user is lost, asks what the AI can do or which skill to use, asks what a skill, hook, memory, or CLAUDE.md means, or asks any other question about how the workspace works.
---

# Help the researcher

Identify the immediate problem. Ask at most two short questions. Then give one direct action.

## Plain-language guide

| Situation | What to say to the AI |
|---|---|
| Start a new project | “Help me set up this project.” The [welcome skill](../welcome/SKILL.md) asks a short interview. |
| Test an idea or run an analysis | “Test whether …” The [experiment skill](../experiment/SKILL.md) records and runs the test. |
| Check whether the work is traceable | “Audit this project.” The [audit skill](../audit/SKILL.md) finds missing evidence and records. |
| See the current state | “Show my research status.” The [status skill](../status/SKILL.md) gives a one-screen view. |
| Clean up files | “Tidy this project.” The [tidy skill](../tidy/SKILL.md) proposes safe moves and archives old files. |
| Understand cleanResearch | “Help me understand …” The **help** skill explains it in plain language. |

## Explain unfamiliar parts

Use an everyday analogy only when it helps. Keep the explanation to four sentences or fewer. Translate every necessary technical term into plain language in the same sentence.

- A **skill** is a saved set of instructions for one kind of task, like a laboratory checklist.
- A **hook** is an automatic action that starts when a named event happens, like a timer that rings when an incubation ends.
- **Memory** is the project’s written notebook of decisions, terms, and preferences. It remains available in later sessions.
- `CLAUDE.md` is the note that tells Claude Code where the project rules are.

Give the smallest next action that solves the user’s current problem. Do not explain unrelated parts.
