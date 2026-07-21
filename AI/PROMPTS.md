# Prompt ledger — Assignment 3, Part B

Record of prompts used to produce the AI-assisted connective tissue. Three workstreams, as required.

---

## 1. Enhanced notebooks and scripts

**Prompt used:**

> I need enhanced Python and R linear regression materials that improve on a basic Salary ~ YearsExperience analysis. Generate command-line scripts and matching Jupyter notebooks that: (1) accept CSV path plus x/y column names as arguments, (2) validate inputs, (3) fit OLS and report intercept, slope, and R², (4) save a clean plot, and (5) run headlessly where relevant. Prefer argparse in Python, avoid deprecated aes_string in R, and use a polished but readable code style. Place outputs as enhanced_linear_regression_* files suitable for an `ai/` folder alongside regression_data.csv.

**Artifacts produced:**

- `enhanced_linear_regression_python.py`
- `enhanced_linear_regression_r.R`
- `enhanced_linear_regression_python.ipynb`
- `enhanced_linear_regression_r.ipynb`

---

## 2. AI code review of the `assignment3` PR diff

**Prompt used:**

> Review the git diff of branch `assignment3` against `main` for repository https://github.com/daltondencklau/BSGP_7030_assignment2. The diff is primarily a new root README.md. Write a formal code-review document (CODE_REVIEW.md) with severity-ranked findings, concrete recommendations, and a clear verdict. Identify at least one substantive issue I should fix if I agree with it. Also note any related quality issues in the inherited Assignment 2 analysis code that a careful reviewer would mention.

**Artifacts produced:**

- `CODE_REVIEW.md`

**Follow-up action from review:**

> Agreed with the critical finding that the root README still begins with a leftover `## README EDITS` heading. Remove that line only; do not rewrite the student’s casual README voice.

---

## 3. AI-generated README from the code

**Prompt used:**

> Generate a sophisticated, academic/professional README from the repository’s linear-regression code and layout. Cover scientific objective, directory architecture, dependencies, how to run the enhanced CLI tools and notebooks, and where Assignment 3 Part B documents live. Use precise technical language and formal structure. Save as `ai/README_AI.md` only — do not overwrite the root `README.md`, which must remain in the student’s own casual voice.

**Artifacts produced:**

- `README_AI.md`

---

## Tone instruction applied across Part B AI prose

> Make AI-authored narrative materials sound highly sophisticated and polished—elevated vocabulary, formal structure, precise technical language—in clear contrast to the student’s informal first-person root README.
