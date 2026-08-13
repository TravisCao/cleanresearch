---
name: tidy
description: Put misplaced or stale cleanResearch files into their correct places without deleting them. Use when the user says the project is messy, files are hard to find, or an audit finds filing or staleness problems.
---

# Tidy the project safely

Use the filing map in [AGENTS.md](../../../AGENTS.md). Preserve every file.

## Plan once

List every misplaced or stale item. For each item, show its current path, proposed destination, reason, and any links that must change. Move stale material to `archive/`. Keep live reusable code only in `src/`.

Show the full move and link-update plan. Ask one confirmation for the complete plan. Do not move anything before that confirmation.

## Apply the plan

Move the confirmed items with your file tools. Never delete them. Update every affected index and relative link. Add an archive note for stale material with its source, move date, and replacement.

Check that all Markdown links resolve and no planned item remains misplaced. Create a Git checkpoint that names the tidy action. Report what moved, what indexes changed, and any item that still needs a researcher decision.
