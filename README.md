## README EDITS
# BSGP 7030 Assignment 2

This is my Assignment 2 repo for BSGP 7030.

I made linear regression models in Python and R using the same dataset (regression_data.csv). The idea was to predict Salary from YearsExperience and see how the two languages compared.

Repo: https://github.com/daltondencklau/BSGP_7030_assignment2

## Assignment 3 links

Main commit before merging assignment3:
https://github.com/daltondencklau/BSGP_7030_assignment2/commit/db8483c81dfed4b27ffb9316a50dd1bfc67a4fa3

assignment3 branch:
https://github.com/daltondencklau/BSGP_7030_assignment2/tree/assignment3

Tagged main after the merge (assignment3-final):
https://github.com/daltondencklau/BSGP_7030_assignment2/releases/tag/assignment3-final

(I’ll update/push the tag after I merge, so that last link might not work until then.)

## Folders

manual/ — the part I did by hand. Has the notebooks, scripts, and data.

manual/Part 2/ — the command line scripts and the plots I saved.

AI/ — the AI-assisted version of the same project.

## What the assignment was about

We learned how to build and compare linear regression models in Python and R with Jupyter notebooks. Using a smaller dataset made it easier to understand what the model was doing.

I used Pandas, Matplotlib, and Scikit-learn in Python. Pandas is good for working with dataframes. Matplotlib is for plotting. Scikit-learn is what I used to actually fit the linear regression. In R I used lm() and ggplot2. I’m less familiar with ggplot, but it’s basically for making plots like Matplotlib.

Part I was notebooks. Part II was turning those into scripts I could run from the terminal.

## Running the AI scripts

cd AI
python linear_regression_python.py regression_data.csv YearsExperience Salary
Rscript linear_regression_r.R regression_data.csv YearsExperience Salary

These print the model results and save the plots.

## Git stuff for Assignment 3

I worked on the assignment3 branch, merged it into main, and tagged the final version as assignment3-final so I could turn in the branch link, the before-merge commit, and the tagged version.

Dalton Dencklau
Text
