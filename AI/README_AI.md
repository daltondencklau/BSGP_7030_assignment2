# BSGP 7030 — Computational Artifact Guide  
### Ordinary Least Squares Across Language Ecosystems

This repository constitutes a reproducible, bilingual demonstration of **univariate linear regression**, contrasting idiomatic workflows in **Python** (pandas / scikit-learn / Matplotlib) and **R** (base `lm` / ggplot2). The empirical vignette relates continuous professional experience to monetary compensation using a compact instructional dataset, thereby isolating model mechanics from confounding data-engineering overhead.

---

## Scientific objective

Given paired observations \((x_i, y_i)\) for \(i = 1,\ldots,n\), estimate parameters \((\beta_0, \beta_1)\) of the classical specification

\[
y_i = \beta_0 + \beta_1 x_i + \varepsilon_i, \quad \varepsilon_i \sim \text{i.i.d.}
\]

and report the coefficient of determination \(R^2\) as a scalar summary of in-sample explanatory power. Parallel implementations enable methodological triangulation: discrepancies, if any, should arise from API conventions rather than statistical substance.

---

## Repository architecture

| Path | Role |
|------|------|
| `manual/` | Author-constructed notebooks, scripts, and derived figures (Assignment 2, Part A) |
| `manual/Part 2/` | Command-line reformulations of the notebook analyses |
| `AI/` | Prior AI-assisted CLI scripts, notebooks, and HTML exports (Assignment 2, Part B) |
| `ai/` *(same directory on case-insensitive volumes)* | Assignment 3 Part B: enhanced analysis entry points, formal documentation, review dossier, and prompt provenance |
| `README.md` | Human-authored project narrative and Assignment 3 citation URLs |

> **Filesystem note.** On macOS default APFS configurations, pathnames `AI/` and `ai/` resolve to a single directory. Part B artifacts are therefore co-located with the earlier `AI/` tree; filenames such as `enhanced_*`, `CODE_REVIEW.md`, `README_AI.md`, and `PROMPTS.md` distinguish Assignment 3 deliverables.

---

## Computational prerequisites

- Python ≥ 3.9 with `pandas`, `matplotlib`, `scikit-learn`
- R ≥ 4.x with **ggplot2**
- Optional: Jupyter kernels for interactive notebook execution

---

## Canonical execution (enhanced interfaces)

```bash
# Python — headless-safe OLS utility
python ai/enhanced_linear_regression_python.py \
  ai/regression_data.csv YearsExperience Salary

# R — lm() + ggplot2 with tidy aesthetic mapping
Rscript ai/enhanced_linear_regression_r.R \
  ai/regression_data.csv YearsExperience Salary
```

Each invocation validates column presence, emits intercept/slope (or a full `summary.lm` report), and writes a high-resolution diagnostic figure.

Legacy entry points remain available under `AI/linear_regression_python.py` and `AI/linear_regression_r.R` for continuity with Assignment 2 submissions.

---

## Interactive notebooks

- `ai/enhanced_linear_regression_python.ipynb` — literate Python exposition of the same estimator  
- `ai/enhanced_linear_regression_r.ipynb` — congruent R notebook with confidence-band visualization  

---

## Assignment 3 provenance artifacts

| Document | Contents |
|----------|----------|
| `ai/CODE_REVIEW.md` | Structured review of the `assignment3` diff versus `main`, including disposition of findings |
| `ai/PROMPTS.md` | Verbatim prompt ledger for enhanced code, review, and this README |
| `ai/README_AI.md` | The present machine-authored technical guide (does **not** replace root `README.md`) |

---

## Interpretive remarks

On the supplied ten-observation sample, a positive slope is expected *a priori*: incremental years of experience covary with higher salary. \(R^2\) on this toy corpus is typically high but should not be over-generalized; the exercise privileges **procedural transparency** and **cross-language parity** over external validity.

---

*Generated as an AI-assisted technical README for BSGP 7030 Assignment 3, Part B. The root `README.md` retains the student’s authentic voice and submission URLs.*
