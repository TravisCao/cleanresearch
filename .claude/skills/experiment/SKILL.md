---
name: experiment
description: Plan, run, freeze, and record a scientific experiment with a complete evidence trail. Use for any analysis, simulation, model run, data transformation, or other run that can affect a scientific conclusion.
---

# Run a traceable experiment

Create the record before the run. Write the expected result before seeing the output.

## 1. Define the test

Read [PROJECT.md](../../../PROJECT.md), [hypotheses.md](../../../hypotheses.md), and [memory/decisions.md](../../../memory/decisions.md). Confirm which hypothesis the run tests. Ask the researcher if the scientific aim is unclear.

Find the highest experiment number in [experiments/INDEX.md](../../../experiments/INDEX.md). Create `experiments/NNN-short-name/` with the next number.

## 2. Write the pre-run record

Create `EXPERIMENT.md` inside the folder. Copy the record fields from [AGENTS.md](../../../AGENTS.md). Before running, complete:

- status: `planned`
- hypothesis ID and link
- date
- expectation and the result that would count against it
- exact command
- input paths
- configuration paths and key settings
- planned output paths

The expectation must exist before any result does.

## 3. Run the test

Set status to `running`. Use code from `src/`. Run the exact recorded command. Keep raw data unchanged.

If the run errors, set status to `failed`. Record the error, where it happened, and any partial output. Add the failed experiment to the index. A failed run is normal scientific evidence. Do not hide it or reuse its number.

## 4. Freeze and interpret

Copy the exact executed code and configuration into the experiment folder. Record the frozen file paths. Do not treat the frozen copies as live code.

Set status to `completed` when the command finishes and the outputs are readable. Add the key numbers and output links under Result. Under Interpretation, state what the result supports, what it counts against, and what it cannot show. Write one concise Insight.

## 5. Connect the evidence

Add one row to [experiments/INDEX.md](../../../experiments/INDEX.md). Add the insight to [insights.md](../../../insights.md). Link the experiment from its hypothesis in [hypotheses.md](../../../hypotheses.md). Ask for explicit confirmation before changing the hypothesis text or state.

Check that every link resolves and that the frozen files match what ran. Create a Git checkpoint with this exact message pattern:

```text
experiment NNN: <name>
```

Report the verdict, key numbers, evidence links, and one suggested next scientific step.
