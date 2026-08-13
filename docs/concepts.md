# Understand your AI in 10 minutes

HonestLab works because it gives your AI a clean desk, clear instructions, and a project notebook. It does not make scientific decisions for you. It helps the AI keep the files and evidence ready for your judgment.

## What an AI agent actually is

An AI agent is an AI assistant that can read files, write files, and run commands on your computer. Claude Code, Codex CLI, and Cursor are examples. Unlike a chat website, an agent can inspect the whole project folder and update the records inside it.

Think of the agent as a capable research assistant working at your desk. It can follow a checklist and organize evidence. It can also misunderstand the science, so you still approve changes to hypotheses and claims.

## The context window is the AI’s working memory

The context window is the information the AI can hold in its working memory during one conversation. Imagine a desk with limited space. The AI can reason about the papers on the desk, but older or less relevant items may leave the desk as more material arrives.

A messy project makes this worse. If five scripts appear to do the same job, the AI must guess which one is current. If a result has no link to its data or settings, the AI may find the number but not its meaning. HonestLab gives each kind of information one fixed place, so the AI can find the right item with less guesswork.

## `AGENTS.md` and `CLAUDE.md` are standing instructions

Imagine a short set of rules taped above the desk. The assistant reads them whenever it starts work.

[`AGENTS.md`](../AGENTS.md) contains the shared HonestLab contract. It tells the AI where files belong, how to record an experiment, how to preserve the exact code that ran, and when it must ask you before changing scientific content. Agents that follow the `AGENTS.md` standard can use these rules.

[`CLAUDE.md`](../CLAUDE.md) is the entry point for Claude Code. It directs Claude Code to the same shared contract and lists the available skills.

## Skills are recipe cards

A skill is a saved set of instructions for one kind of job. Think of six recipe cards kept beside the desk. The AI pulls out the relevant card when you ask for that job.

- [`welcome`](../.claude/skills/welcome/SKILL.md) asks a short interview and fills the project context.
- [`help`](../.claude/skills/help/SKILL.md) explains the workspace and gives one direct next action.
- [`experiment`](../.claude/skills/experiment/SKILL.md) plans, runs, freezes, and records a scientific test.
- [`audit`](../.claude/skills/audit/SKILL.md) checks claims, experiment records, figures, old results, links, and file locations.
- [`status`](../.claude/skills/status/SKILL.md) shows the current research state on one screen.
- [`tidy`](../.claude/skills/tidy/SKILL.md) proposes safe file moves, asks for approval, and preserves old material.

The card does not replace judgment. It makes the repeated file and record work consistent.

## Hooks are automatic event rules

A hook is an automatic rule that runs when a named event occurs. It is like a laboratory timer that rings after a fixed step. For example, a future hook could check that an experiment record exists before an analysis command runs, or check that changed Markdown links still work after a file edit.

HonestLab does not ship any hooks today. The current skills and `AGENTS.md` tell the AI what to do, but they do not technically block an incorrect action. This is why the audit workflow matters.

## Memory files are the project notebook

The [`memory/`](../memory/) folder is the notebook that stays with the project after a conversation ends.

- `decisions.md` records what you decided, when you decided it, and why.
- `glossary.md` records important terms in the meanings that your project uses.
- `preferences.md` records how you want the AI to reply and work.

These files prevent you from explaining the same background in every conversation. `preferences.md` is also portable: you can copy your preferred language, level of detail, and working choices into a new project, then adjust the project-specific parts.

## Five habits that keep the AI’s context clean

1. **Keep one topic in each chat session.** Start a new session when you move from an experiment to an unrelated task.
2. **Ask for status when you return.** Say “Show my research status” so the AI reloads the project question, hypotheses, recent experiments, newest insight, and next step.
3. **Let tidy run each month.** Say “Tidy this project.” Review the proposed moves, then approve the plan if it is correct.
4. **Keep files small and focused.** One file should have one clear purpose. Put reusable code in `src/` and experiment records in `experiments/`.
5. **Reset the instructions when the AI seems confused.** Say “Re-read `AGENTS.md`, then tell me the current project state before doing anything else.”

The simplest test is already in the repository. Open [E001](../experiments/001-first-example/EXPERIMENT.md) and follow its links from hypothesis to command, input, frozen code, settings, outputs, result, and insight.
