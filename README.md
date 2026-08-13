<img src="assets/logo.svg" width="96">

# cleanResearch

**Your AI assistant stops getting confused by your own project — and every result keeps its receipts.**

Traceable, auditable, AI-native research.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
![Works with Claude Code, Codex, and Cursor](https://img.shields.io/badge/works%20with-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20Cursor-555.svg)

[中文版](README.zh-CN.md)

cleanResearch is an AI-native research workspace. It is a GitHub template where one folder holds one research project. It gives your AI a fixed structure and a paper trail from claim to insight to experiment to the exact code, data, and settings that produced the result. You judge the science. The AI maintains the records.

## The pain

- Your AI wrote 30 scripts. Which one is current?
- You found a figure. Which data and settings produced it?
- The agent confidently cites a result that a later test replaced.
- A reviewer asks where a number came from. You cannot defend an answer that your AI produced.

## What you get

- A fixed place for your research question, hypotheses, data notes, code, experiments, insights, claims, decisions, and references.
- A recorded experiment workflow that writes the expectation before the run and records the exact command, inputs, settings, result, and limits.
- A frozen copy of the code and settings used for each experiment, while the current reusable code stays in `src/`.
- Evidence links from manuscript claims back to experiment records and outputs.
- Six ready-made workflows for setup, help, experiments, audits, status, and safe cleanup.

## Start in 30 seconds

You need [Git](https://git-scm.com/) and an AI coding agent that can read and write files: Claude Code, Codex CLI, or Cursor.

### Paste this into your AI agent

> Clone `https://github.com/TravisCao/cleanresearch` into a folder named after my project. Remove the cloned `.git` folder, run `git init`, and make the first commit. Read `AGENTS.md`. Then run the welcome interview from `.claude/skills/welcome/SKILL.md`. Explain any action I need to take in plain language.

Your AI handles the remaining setup.

## Works with

- **Claude Code:** Open the project folder and say, “Run the welcome interview.”
- **Codex:** Add the project folder to Codex and say, “Run the welcome interview.”

### Or use the GitHub template

1. Open [cleanResearch on GitHub](https://github.com/TravisCao/cleanresearch) and select **Use this template**.
2. Open your AI coding agent in the new project folder.
3. Say: “Run the welcome interview.”

## Your first 10 minutes

1. Complete the welcome interview. Your AI fills the project description, glossary, and working preferences.
2. Describe something you want to test in plain words: “I want to test whether …”
3. Let the AI run it as a recorded experiment. It writes the expectation first, runs the command, then keeps the result and the exact files that produced it.
4. Ask: “What evidence do we have for my hypothesis, and how was each result produced?”
5. Say: “Audit the project.” The AI checks for missing evidence, unknown figure sources, incomplete records, and stale citations.

You can inspect the shipped [E001 example](experiments/001-first-example/EXPERIMENT.md) immediately. It uses generated step-count data to show a complete experiment record. Prefer to read a full session first? See the [annotated demo transcript](docs/demo-transcript.md). Stop there. You will know if cleanResearch is for you.

## You say → what happens

| You say | What happens |
|---|---|
| “Run the welcome interview.” | The AI asks up to seven short questions and fills the project context. |
| “Help me understand this workspace.” | The help workflow explains the relevant part and gives one next action. |
| “I want to test whether …” | The AI connects the test to a hypothesis and prepares a numbered experiment record. |
| “Run this analysis as an experiment.” | The AI records the expectation and command before the run, then records and links the result. |
| “Show my research status.” | The AI shows the question, active hypotheses, three latest experiments, newest insight, and one next step. |
| “Audit the project.” | The AI checks claims, experiments, figures, old results, file locations, links, and frozen files. |
| “Tidy this project.” | The AI proposes safe file moves, asks once for approval, then moves files and updates links without deleting them. |
| “What does ‘frozen code’ mean?” | The help workflow explains the term in plain language. |
| “Where did this figure come from?” | The AI checks whether the figure links to an experiment output and reports any missing source. |

## What’s in the box

```text
cleanresearch/
├── .claude/skills/          single source for the six task instructions
├── .codex/skills/           link that gives Codex the same task instructions
├── assets/                  logo files used by the project guide
├── docs/                    plain-language guides and demonstrations
├── AGENTS.md                shared rules for AI coding agents
├── CLAUDE.md                entry point that sends Claude Code to the shared rules
├── CONTRIBUTING.md          contribution requirements
├── LICENSE                  MIT license terms
├── PROJECT.md               research question, scope, data, and methods
├── README.md                English setup and first-use guide
├── README.zh-CN.md          Simplified Chinese setup and first-use guide
├── hypotheses.md            active and retired testable statements
├── insights.md              short conclusions linked to experiments
├── data/
│   ├── DATA.md              data sources, contents, changes, and limits
│   ├── raw/                 unchanged input data
│   └── processed/           data created from the raw inputs
├── experiments/
│   ├── INDEX.md             one-line register of every experiment
│   └── 001-first-example/   finished example with code, settings, and outputs
├── src/                     current reusable analysis code
├── manuscript/
│   ├── claims.md            proposed and supported claims with evidence links
│   └── figures/             figures linked to experiment outputs
├── memory/                  decisions, project terms, and working preferences
├── references/              index of papers and other sources
└── archive/                 replaced material kept for the record
```

## How it stays organized

- **Record before the run.** The experiment file states the hypothesis, expectation, command, inputs, and settings before results exist.
- **Freeze what ran.** Each experiment keeps a copy of the executed code and configuration.
- **Mark stale things.** Replaced experiments become `superseded`, and old files move to `archive/` instead of disappearing.
- **No claim without evidence.** Each manuscript claim must cite an experiment ID, and each figure must link to its source output.

These are instructions for the AI, not a guarantee. The researcher still judges the method and conclusion. Read [Understand your AI in 10 minutes](docs/concepts.md) for a plain-language tour.

## Who it’s for / who it’s not for

cleanResearch is for researchers in any field who work with AI coding agents and want a clear local record of how each result was produced. You do not need to be a programmer.

It is not for teams that need MLflow-scale experiment tracking, shared compute management, or access controls. It is also not useful if you never use an AI agent that can work with local files.

## FAQ

Read the [frequently asked questions](docs/faq.md).

## Roadmap

- Hooks that automatically check whether new work was filed correctly.
- A manuscript-writing workflow that follows the evidence links.
- Field packs with examples and instructions for common research areas.
- A continuous integration audit that checks the project on GitHub.

These items are planned. They are not included today.

## License

cleanResearch uses the [MIT License](LICENSE).
