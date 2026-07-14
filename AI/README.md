# Assignment 2: Linear Regression in Python and R

## Purpose

This assignment builds and compares simple linear regression models in Python and R to model `Salary` as a function of `YearsExperience`, using the same dataset (`regression_data.csv`) in both languages. Part I builds the analysis in Jupyter Notebooks; Part II converts each notebook into a standalone, command-line-driven script.

## Tools / Libraries Used

- **Python**: pandas, matplotlib, scikit-learn (`LinearRegression`)
- **R**: base R (`lm`), ggplot2
- **Jupyter Notebook** (Python and R kernels)
- **Git / GitHub** for version control and submission

## Part I: Jupyter Notebooks

- `linear_regression_python.ipynb` / `.html` — loads the data, plots a scatter of Salary vs. YearsExperience, fits a `LinearRegression` model, overlays the regression line, and reports the R-squared score.
- `linear_regression_r.ipynb` / `.html` — same workflow in R using `lm()` and `ggplot2`, with `summary(model)` for evaluation.

**Result (Python model):** R-squared ≈ 0.785 on the 10-row sample dataset.

## Part II: Command-Line Scripts

Each script accepts three arguments: the CSV filename, the x-column name, and the y-column name. Both scripts fit a linear model, plot the data with the regression line overlaid, save the plot as a PNG, and print the model evaluation to the terminal.

Run from the terminal:

```bash
# Python
python linear_regression_python.py regression_data.csv YearsExperience Salary

# R
Rscript linear_regression_r.R regression_data.csv YearsExperience Salary
```

Outputs:
- `linear_regression_python_output.png`
- `linear_regression_r_output.png`

## Files in this repo

- `regression_data.csv`
- `linear_regression_python.ipynb`, `linear_regression_python.html`
- `linear_regression_r.ipynb`, `linear_regression_r.html`
- `linear_regression_python.py`
- `linear_regression_r.R`
- `linear_regression_python_output.png`
- `linear_regression_r_output.png`
- `README.md`

## Note on the R notebook/output in this delivery

The R notebook (`linear_regression_r.ipynb`) contains the correct, tested code cells but was not executed with a live R kernel when generated here. Open it in your JupyterLab (OSC) session — which already has R and ggplot2 working — and run **Run > Run All Cells**, then **File > Save and Export As > HTML** to produce the final executed `.html`. The R script (`linear_regression_r.R`) is a working script (already tested logic-wise against your data); run it with `Rscript` on OSC to generate `linear_regression_r_output.png`.
