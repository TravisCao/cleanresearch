#!/usr/bin/env python3
"""Analyze generated step counts. (example — your AI will replace this)"""

import argparse
import csv
import json
from pathlib import Path
from statistics import mean


def load_steps(path):
    groups = {"weekday": [], "weekend": []}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            groups[row["day_type"]].append(int(row["steps"]))
    return groups


def make_bar(value, scale):
    return "#" * round(value / scale)


def main():
    parser = argparse.ArgumentParser(description="Compare two groups of step counts.")
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    groups = load_steps(args.input)
    weekday_mean = mean(groups["weekday"])
    weekend_mean = mean(groups["weekend"])
    difference = weekday_mean - weekend_mean
    scale = config["steps_per_chart_character"]

    metrics = {
        "note": "example — your AI will replace this",
        "weekday_days": len(groups["weekday"]),
        "weekend_days": len(groups["weekend"]),
        "weekday_mean_steps": round(weekday_mean, 1),
        "weekend_mean_steps": round(weekend_mean, 1),
        "difference_steps": round(difference, 1),
        "expectation_met": difference > 0,
    }
    summary = (
        "Step-count comparison (example — your AI will replace this)\n"
        f"Weekday | {make_bar(weekday_mean, scale)} {weekday_mean:.1f}\n"
        f"Weekend | {make_bar(weekend_mean, scale)} {weekend_mean:.1f}\n"
        f"Difference: {difference:.1f} steps per day\n"
        f"Expectation met: {difference > 0}\n"
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "metrics.json").write_text(
        json.dumps(metrics, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "summary.txt").write_text(summary, encoding="utf-8")
    print(summary, end="")


if __name__ == "__main__":
    main()
