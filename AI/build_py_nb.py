import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

cells.append(nbf.v4.new_markdown_cell(
"This notebook demonstrates a simple linear regression analysis using Python to model Salary based on Years of Experience."
))

cells.append(nbf.v4.new_markdown_cell("## Step 1: Load and inspect the dataset"))
cells.append(nbf.v4.new_code_cell(
"import pandas as pd\n"
"dataset = pd.read_csv(\"regression_data.csv\")\n"
"dataset"
))

cells.append(nbf.v4.new_markdown_cell("## Step 2: Scatter plot of Years of Experience vs. Salary"))
cells.append(nbf.v4.new_code_cell(
"import matplotlib.pyplot as plt\n"
"plt.scatter(dataset[\"YearsExperience\"], dataset[\"Salary\"], color=\"red\")\n"
"plt.title(\"Salary vs Experience\")\n"
"plt.xlabel(\"Years of Experience\")\n"
"plt.ylabel(\"Salary\")\n"
"plt.show()"
))

cells.append(nbf.v4.new_markdown_cell("## Step 3: Fit a linear regression model"))
cells.append(nbf.v4.new_code_cell(
"from sklearn.linear_model import LinearRegression\n"
"model = LinearRegression()\n"
"model.fit(dataset[[\"YearsExperience\"]], dataset[[\"Salary\"]])"
))

cells.append(nbf.v4.new_markdown_cell("## Step 4: Overlay the regression line on the scatter plot"))
cells.append(nbf.v4.new_code_cell(
"plt.scatter(dataset[\"YearsExperience\"], dataset[\"Salary\"], color=\"red\")\n"
"plt.plot(dataset[\"YearsExperience\"], model.predict(dataset[[\"YearsExperience\"]]), color=\"blue\")\n"
"plt.title(\"Salary vs Experience\")\n"
"plt.xlabel(\"Years of Experience\")\n"
"plt.ylabel(\"Salary\")\n"
"plt.show()"
))

cells.append(nbf.v4.new_markdown_cell("## Step 5: Evaluate the model (R-squared)"))
cells.append(nbf.v4.new_code_cell(
"model.score(dataset[[\"YearsExperience\"]], dataset[[\"Salary\"]])  # R-squared"
))

nb['cells'] = cells
with open("linear_regression_python.ipynb", "w") as f:
    nbf.write(nb, f)
print("notebook written")
