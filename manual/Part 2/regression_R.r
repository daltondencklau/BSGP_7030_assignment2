## reading the df and loading data
df <- read.csv("regression_data.csv")
df

## creating a scatter plot based on years of experience and salary
plot(df$YearsExperience, df$Salary, col = "red")

## fitting a linear model to our data
model <- lm(Salary ~ YearsExperience, data=df)

## installing ggplot
install.packages("ggplot2", repos = "https://cloud.r-project.org")

## opening library
library(ggplot2)

ggplot()+
    geom_point(aes(x = df$YearsExperience, y = df$Salary), colour = 'red') +
    geom_line(aes(x = df$YearsExperience, y = predict(model, newdata = df)), colour = 'blue') +
    ggtitle ('Salary v. Experience') +
    xlab('Years of Experience') +
    ylab('Salary')

## evaluating the model
summary(model)

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 3) {
  stop("Usage: Rscript linear_regression_r.R <filename> <x_column> <y_column>")
}

filename <- args[1]
x_col <- args[2]
y_col <- args[3]

data <- read.csv(filename)
formula <- as.formula(paste(y_col, "~", x_col))
model <- lm(formula, data = data)

library(ggplot2)
plot <- ggplot(data, aes_string(x = x_col, y = y_col)) +
  geom_point(color = "red") +
  geom_smooth(method = "lm", color = "blue") +
  ggtitle(paste(y_col, "vs", x_col)) +
  xlab(x_col) +
  ylab(y_col)

ggsave("linear_regression_r_output.png", plot)
print(plot)