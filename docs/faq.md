# Frequently asked questions

## Do I need to know how to code?

No. Describe the research task in plain language. Your AI reads and writes the files, runs commands, and explains what it did. You still judge the research question, method, and conclusion.

## Do I need to know Git?

No. Git is the tool that saves named checkpoints of your project. It must be installed. If it is missing, ask your AI to install it and handle the commands.

## Does my data leave my computer?

The ResearchOS workspace consists of plain local files. ResearchOS does not upload them. The AI service you choose may process file contents under its own data policy, so check that vendor’s policy before using private or restricted data.

## Which AI agents work?

ResearchOS is designed for Claude Code, Codex CLI, and Cursor. The shared instructions live in `AGENTS.md`; `CLAUDE.md` directs Claude Code to those rules. Other file-based agents may work if they read `AGENTS.md`, but this template does not test or promise support for them.

## I use Codex, not Claude Code - does this work?

Yes. Add the project folder to Codex and say, “Run the welcome interview.” Codex reads the shared rules from `AGENTS.md` and finds the same six workflows under `.codex/skills/` that Claude Code uses under `.claude/skills/`.

## Can I use the ChatGPT or Claude website alone?

No. You need an AI agent that can read and write files in the project folder. A chat website cannot maintain the local workspace by itself.

## I already have a messy project. What should I do?

Start a fresh project from the template. Then ask your AI to migrate your files into it with the `tidy` workflow. Review the complete move plan before you approve it. The workflow preserves files and moves stale material to `archive/` instead of deleting it.

## What if the AI ignores the rules?

The rules are strong defaults, not guarantees. Run “Audit this project” each week and before you share work. The audit checks for unsupported claims, incomplete experiments, unknown figure sources, stale citations, misplaced files, broken links, and missing frozen files.

## Does ResearchOS work on Windows?

Yes. The workspace uses plain files and Git. Prefer the paste-to-your-AI installation path in the [README](../README.md), so your agent can use commands that match your computer.

## Is ResearchOS free?

Yes. ResearchOS uses the [MIT License](../LICENSE), which permits use, modification, and distribution under its terms. Your AI provider may charge separately.

## How do I update the template later?

You do not need to. After you clone or create a project from the template, that project is yours. You can copy a future skill or document into it if you want a later feature, but normal research work does not depend on template updates.
