# ResearchOS demo transcript

> **Illustrative transcript — your session will differ. The example experiment it references, 001, is real and ships in this template.**

## Scene 1 — Welcome interview

> **Researcher:** Help me set up this project.
>
> **ResearchOS:** What is your research field?
>
> **Researcher:** Behavioral science.
>
> **ResearchOS:** What is your main research question in one sentence?
>
> **Researcher:** Is daily step count higher on weekdays than on weekends?
>
> **ResearchOS:** What data do you have now?
>
> **Researcher:** A generated file with daily step counts for 60 days.
>
> **ResearchOS:** I’ll record the question and data in `PROJECT.md`, and your working terms and reply preferences in `memory/`. Before I add H1 to `hypotheses.md`, do you confirm this wording: “Daily step count is higher on weekdays than on weekends”?

*Annotation: The welcome skill collected the project context, but ResearchOS still asks the researcher before it changes a hypothesis.*

## Scene 2 — Run a traceable experiment

> **Researcher:** Yes. Test it by comparing the average weekday and weekend step counts.
>
> **ResearchOS:** I found no earlier experiment, so this will be E001. I created `experiments/001-first-example/EXPERIMENT.md` before running the analysis. Its pre-run record says:
>
> ```markdown
> ## Expectation — written before the run
>
> The weekday mean will be higher than the weekend mean. A difference of zero or less will count against H1.
> ```
>
> The planned command is:
>
> ```text
> python3 experiments/001-first-example/analyze_steps.py --input data/raw/example-steps.csv --config experiments/001-first-example/config.json --output-dir experiments/001-first-example/outputs
> ```
>
> I will now run that exact command, preserve the executed code and configuration in the experiment folder, and record the outputs.
>
> **ResearchOS:** The run completed. The weekday mean was 9,000 steps across 44 days. The weekend mean was 6,200 steps across 16 days. The difference was 2,800 steps per day, so the expectation was met. This supports H1 only within the generated example data; it does not show a pattern in real people.

*Annotation: The expectation was recorded before the run. This is rule 4 of `AGENTS.md`; the saved code and configuration apply rule 6.*

## Scene 3 — Trace the evidence

> **Researcher:** What evidence do we have for my hypothesis and how was each result produced?
>
> **ResearchOS:** H1 is supported only by the generated example data. Here is the complete chain:
>
> 1. **Hypothesis:** `hypotheses.md` links H1 to E001.
> 2. **Insight:** `insights.md` records that the weekday mean was 2,800 steps per day higher in this example.
> 3. **Experiment record:** `experiments/001-first-example/EXPERIMENT.md` records the expectation, method, result, interpretation, and limits.
> 4. **Input:** `data/raw/example-steps.csv` contains 60 rows: 44 weekdays and 16 weekend days.
> 5. **Executed files:** `experiments/001-first-example/analyze_steps.py` and `experiments/001-first-example/config.json` preserve the code and the setting of 400 steps per chart character.
> 6. **Outputs:** `experiments/001-first-example/outputs/metrics.json` reports `weekday_mean_steps: 9000`, `weekend_mean_steps: 6200`, `difference_steps: 2800`, and `expectation_met: true`. The readable output is `experiments/001-first-example/outputs/summary.txt`.
>
> The script grouped the input rows by day type, calculated each mean, and subtracted the weekend mean from the weekday mean. The evidence supports a difference in this generated data. It does not support a health claim or a conclusion about real people.

*Annotation: The request followed the evidence chain from H1 to the recorded insight, then to E001 and the exact input, code, configuration, and outputs.*

## Scene 4 — Audit before sharing

> **Researcher:** I added “Weekday schedules cause people to walk more” to `manuscript/claims.md`. Audit the project before I share it.
>
> **ResearchOS:** I found one problem that can invalidate a claim:
>
> - **Location:** `manuscript/claims.md`
> - **Problem:** “Weekday schedules cause people to walk more” has no experiment ID, and E001 compares generated groups without testing cause.
> - **Effect:** A reader cannot trace this causal claim to supporting evidence.
> - **Fix:** Keep it under “Proposed,” or replace it with the supported descriptive claim: “In the generated example data, the mean daily step count is 2,800 steps higher on weekdays than on weekends.” Cite E001.
>
> I did not change the claim. Do you want me to replace it with the supported wording?

*Annotation: The audit skill checked claim-to-experiment links and kept the researcher in control of scientific wording.*
