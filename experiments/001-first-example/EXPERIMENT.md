# E001: First example *(example — your AI will replace this)*

What this file is: the complete record of one scientific run. Who writes it: your AI before and after the run. When you read it: when you want to inspect the method, result, or evidence.

Status: completed  
Hypothesis: [H1 — Daily step count is higher on weekdays than on weekends](../../hypotheses.md#h1-daily-step-count-is-higher-on-weekdays-than-on-weekends-example--your-ai-will-replace-this)  
Date: 2026-08-13

## Expectation — written before the run

The weekday mean will be higher than the weekend mean. A difference of zero or less will count against H1.

## Method

- Exact command: `python3 experiments/001-first-example/analyze_steps.py --input data/raw/example-steps.csv --config experiments/001-first-example/config.json --output-dir experiments/001-first-example/outputs`
- Inputs: [example-steps.csv](../../data/raw/example-steps.csv)
- Configuration: [config.json](config.json), with 400 steps per chart character
- Frozen code: [analyze_steps.py](analyze_steps.py)
- Live code source: [src/analyze_steps.py](../../src/analyze_steps.py)

The script groups the 60 rows by day type. It calculates the mean for each group and subtracts the weekend mean from the weekday mean.

## Result

The weekday mean was 9,000 steps across 44 days. The weekend mean was 6,200 steps across 16 days. The difference was 2,800 steps per day, so the expectation was met.

Outputs: [metrics.json](outputs/metrics.json) and [summary.txt](outputs/summary.txt).

## Interpretation

The generated data support H1 within this example. The result does not show a pattern in real people because the data were made for demonstration.

## Insight

In the generated example data, weekday step counts were higher than weekend step counts by a mean of 2,800 steps per day.
