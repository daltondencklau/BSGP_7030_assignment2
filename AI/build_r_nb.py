import nbformat as nbf

nb = nbf.v4.new_notebook()
nb['metadata'] = {
  "kernelspec": {
    "display_name": "R",
    "language": "R",
    "name": "ir"
  },
  "language_info": {
    "name": "R"
  }
}
cells = []

cells.append(nbf.v4.new_markdown_cell(
"This notebook demonstrates a simple linear regression analysis using R to model Salary based on Years of Experience."
))

cells.append(nbf.v4.new_markdown_cell("## Step 1: Load and inspect the dataset"))
cells.append(nbf.v4.new_code_cell(
"dataset <- read.csv(\"regression_data.csv\")\n"
"dataset"
))

cells.append(nbf.v4.new_markdown_cell("## Step 2: Scatter plot of Years of Experience vs. Salary"))
cells.append(nbf.v4.new_code_cell(
"plot(dataset$YearsExperience, dataset$Salary, col=\"red\",\n"
"     main=\"Salary vs Experience\", xlab=\"Years of Experience\", ylab=\"Salary\")"
))

cells.append(nbf.v4.new_markdown_cell("## Step 3: Fit a linear regression model"))
cells.append(nbf.v4.new_code_cell(
"model <- lm(Salary ~ YearsExperience, data=dataset)\n"
"model"
))

cells.append(nbf.v4.new_markdown_cell("## Step 4: Overlay the regression line on the scatter plot"))
cells.append(nbf.v4.new_code_cell(
"install.packages(\"ggplot2\", repos = \"https://cloud.r-project.org\")\n"
"library(ggplot2)\n"
"ggplot() +\n"
"  geom_point(aes(x = dataset$YearsExperience, y = dataset$Salary), colour = 'red') +\n"
"  geom_line(aes(x = dataset$YearsExperience, y = predict(model, newdata = dataset)), colour = 'blue') +\n"
"  ggtitle('Salary vs Experience') +\n"
"  xlab('Years of experience') +\n"
"  ylab('Salary')"
))

cells.append(nbf.v4.new_markdown_cell("## Step 5: Evaluate the model"))
cells.append(nbf.v4.new_code_cell(
"summary(model)"
))

nb['cells'] = cells
with open("linear_regression_r.ipynb", "w") as f:
    nbf.write(nb, f)
print("R notebook written (unexecuted - no R kernel available in this sandbox)")
