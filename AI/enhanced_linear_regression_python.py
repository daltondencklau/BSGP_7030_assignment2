#!/usr/bin/env python3
"""
Command-line ordinary least squares (OLS) regression utility.

Fits a univariate linear model of the form y ~ x from a CSV input, reports
coefficient estimates and R², and persists a publication-ready scatter/fit plot.
Designed for headless execution (e.g., HPC login nodes) via a non-interactive
Matplotlib backend.
"""

from __future__ import annotations

import argparse
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Estimate a simple linear regression from tabular data and export "
            "a diagnostic scatter plot with the fitted response surface."
        )
    )
    parser.add_argument("filename", help="Path to the input CSV file")
    parser.add_argument("x_column", help="Name of the predictor (explanatory) column")
    parser.add_argument("y_column", help="Name of the response (outcome) column")
    parser.add_argument(
        "-o",
        "--output",
        default="enhanced_linear_regression_python_output.png",
        help="Destination path for the rendered figure",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        data = pd.read_csv(args.filename)
    except FileNotFoundError:
        print(f"Error: input file not found: {args.filename}", file=sys.stderr)
        return 1

    missing = [c for c in (args.x_column, args.y_column) if c not in data.columns]
    if missing:
        print(
            f"Error: missing column(s) {missing}. Available: {list(data.columns)}",
            file=sys.stderr,
        )
        return 1

    x = data[[args.x_column]]
    y = data[args.y_column]

    model = LinearRegression()
    model.fit(x, y)
    y_hat = model.predict(x)
    r_squared = model.score(x, y)

    fig, ax = plt.subplots(figsize=(7.5, 5.0))
    ax.scatter(x, y, color="#c0392b", alpha=0.85, label="Observations")
    ax.plot(x, y_hat, color="#2980b9", linewidth=2.0, label="OLS fit")
    ax.set_title(f"{args.y_column} as a function of {args.x_column}")
    ax.set_xlabel(args.x_column)
    ax.set_ylabel(args.y_column)
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(args.output, dpi=160)
    plt.close(fig)

    print(f"Dataset: {args.filename} (n = {len(data)})")
    print(f"Specification: {args.y_column} ~ {args.x_column}")
    print(f"Intercept (β₀): {model.intercept_:.6f}")
    print(f"Slope (β₁):     {model.coef_[0]:.6f}")
    print(f"Coefficient of determination (R²): {r_squared:.6f}")
    print(f"Figure written to: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
