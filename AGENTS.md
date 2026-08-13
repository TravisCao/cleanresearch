# ResearchOS agent contract

What this file is: the rules for every AI that works in this project. Who writes it: the ResearchOS maintainers. When you read it: at the start of every session and before any scientific work.

The researcher judges the science. You maintain the files, links, and evidence trail. Always follow these ten rules.

## Ten rules

1. **Start with the project state.** Read [PROJECT.md](PROJECT.md), [hypotheses.md](hypotheses.md), and [memory/decisions.md](memory/decisions.md). Then greet the researcher with the research question, the active hypotheses, the latest experiment, and one suggested next step. When the researcher starts a real project, offer to archive the example.

2. **File every item in its fixed place.** Keep project scope in `PROJECT.md`, hypotheses in `hypotheses.md`, insights in `insights.md`, runs in `experiments/`, reusable code in `src/`, data notes in `data/DATA.md`, sources in `references/`, claims and figures in `manuscript/`, durable context in `memory/`, and old material in `archive/`. Keep no loose research files at the root.

3. **Keep one live copy of code.** Treat `src/` as the only place for live, reusable code. Extend code that exists there. Do not create a second live implementation of the same method.

4. **Create the experiment record before the run.** For every run that can affect a scientific conclusion, create `experiments/NNN-short-name/` first. Write the hypothesis, date, method, exact command, inputs, configuration, and expected result before you run anything. Use the record template below.

5. **Complete the record after the run.** Record the result, interpretation, and one concise insight. Add one line to [experiments/INDEX.md](experiments/INDEX.md). Add the insight to [insights.md](insights.md). Link the experiment from its hypothesis in [hypotheses.md](hypotheses.md).

6. **Freeze exactly what ran.** Copy the executed code and configuration into the experiment folder. Keep the input and output paths in the record. Then create a Git commit, which is a named checkpoint of the files, with the message `experiment NNN: <name>`.

7. **Make old results visibly old.** Mark replaced experiments `superseded`. Move dead code to `archive/`. Never cite a superseded result in an insight, figure, or claim. Preserve old material so the history stays clear.

8. **Require evidence for claims.** Every manuscript claim must cite one or more experiment IDs, such as `E001`. Refuse to write or keep a scientific claim that has no experiment evidence. Link each figure to the experiment output that produced it.

9. **Record human decisions.** Add each research decision to [memory/decisions.md](memory/decisions.md). Include the date, the decision, and the reason in the researcher’s words. Keep terms in [memory/glossary.md](memory/glossary.md) and communication choices in [memory/preferences.md](memory/preferences.md).

10. **Keep the researcher in control.** Explain every action in plain language because the researcher is not a programmer. Ask for explicit confirmation in the current conversation before you change a hypothesis, change a manuscript claim, or delete any data. Archive files instead of deleting them when possible.

## Experiment record template

Create `experiments/NNN-short-name/EXPERIMENT.md` with these fields before a consequential run:

```markdown
# E<NNN>: <short name>

Status: planned | running | completed | failed | superseded
Hypothesis: H<number> — <linked hypothesis>
Date: YYYY-MM-DD

## Expectation — written before the run

State what result you expect and what result would count against the hypothesis.

## Method

- Exact command: `<command>`
- Inputs: `<paths>`
- Configuration: `<paths and key settings>`
- Frozen code: `<copy inside this experiment folder>`

## Result

Give the key numbers and link every output.

## Interpretation

State what the result does and does not show.

## Insight

Write one reusable conclusion in one or two sentences.
```

## Skills

- [welcome](.claude/skills/welcome/SKILL.md): start a new project through a short interview.
- [help](.claude/skills/help/SKILL.md): explain ResearchOS and choose the right action.
- [experiment](.claude/skills/experiment/SKILL.md): plan, run, freeze, and record a scientific experiment.
- [audit](.claude/skills/audit/SKILL.md): check the evidence trail before sharing work.
- [status](.claude/skills/status/SKILL.md): show the current research state on one screen.
- [tidy](.claude/skills/tidy/SKILL.md): move misplaced or stale files without deleting them.
