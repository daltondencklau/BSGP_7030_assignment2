# Automated Code Review — `assignment3` ∥ `main`

**Scope.** Comparative inspection of `origin/main...assignment3` (the prospective pull-request delta), with ancillary commentary on contiguous analysis artifacts already present on `main` that the branch inherits.

**Base.** `main` @ `db8483c` — *AI Portion of Assignment 2*  
**Head.** `assignment3` @ current tip — README authorship + Assignment 3 linkage metadata  
**Diff composition.** Effectively a single new root document (`README.md`); no algorithmic changes in the primary delta.

---

## Executive assessment

The branch accomplishes its pedagogical objective—documenting repository purpose and supplying the three required GitHub citation URLs—with commendable clarity of authorial voice. Nonetheless, several defects of polish and repository hygiene merit remediation before the pull request is regarded as merge-complete relative to remote `main`.

---

## Findings

### 1. Residual drafting artifact in the root README *(severity — addressed)*

The file opens with a vestigial heading:

```markdown
## README EDITS
```

This fragment is unmistakably an editorial leftover rather than intentional exposition. It degrades first-impression professionalism and will confuse automated README renderers / graders scanning for an H1 title.

**Recommendation.** Excise the stray heading so the document begins at `# BSGP 7030 Assignment 2`.

**Disposition.** **Accepted and applied** on this branch (see accompanying commit). The casual authorial tone of the remainder of the README is preserved unchanged.

### 2. Semantic drift between narrative and remote branch topology *(major)*

The README asserts that `assignment3` was merged into `main` and tagged `assignment3-final`. Empirically, remote `main` remains at `db8483c` while `assignment3` is several commits ahead. The annotated tag exists, but it does not currently decorate remote `main`.

**Recommendation.** Either (a) fast-forward / merge `assignment3` into `main` and `git push origin main`, updating prose only after the remote reflects that state, or (b) revise the README wording to “pending merge / local merge completed; remote main not yet updated” until the push lands.

### 3. Stale parenthetical regarding the tag URL *(minor)*

The note *“I’ll update/push the tag after I merge…”* is obsolete once `assignment3-final` has been created and pushed. Retaining it undercuts confidence in the submission links.

**Recommendation.** Delete the parenthetical once the release/tag URL resolves in the browser.

### 4. Inherited CLI robustness gaps outside the strict PR diff *(informational)*

Although outside the narrow `README.md` delta, reviewers examining the full Assignment 2 corpus will observe that early manual Python exports embed notebook residue (`pip install` cells, malformed `.format` strings, hardcoded CSV paths). The pre-existing `AI/` CLI scripts are substantially sounder; the new enhanced scripts introduced under this Part B pass further harden argument parsing, headless plotting, and column validation.

**Recommendation.** Prefer the enhanced CLI entry points for demonstration; treat the raw notebook exports as historical process artifacts.

### 5. ggplot2 aesthetic API currency *(informational)*

`AI/linear_regression_r.R` still relies on `aes_string()`, which is soft-deprecated. The enhanced R script migrates to `.data[[col]]` tidy evaluation.

---

## Summary table

| ID | Severity | Topic | Status |
|----|----------|-------|--------|
| 1 | Critical | Stray `## README EDITS` heading | **Fixed** |
| 2 | Major | README claims merge; remote `main` lagging | Open — user push/PR |
| 3 | Minor | Obsolete “tag not pushed yet” note | Suggested |
| 4 | Info | Manual script fragility | Mitigated via enhanced scripts |
| 5 | Info | `aes_string` deprecation | Mitigated in enhanced R script |

---

## Verdict

Approve **after** (i) removal of the drafting heading (done) and (ii) alignment of remote `main` with the tagged tip, or clarification of wording. The Assignment 3 documentation itself is pedagogically adequate and appropriately first-person; Part B materials below supply the more formal technical register expected of AI-assisted connective tissue.
