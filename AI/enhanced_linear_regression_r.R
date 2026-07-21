#!/usr/bin/env Rscript
# Enhanced command-line OLS regression in R.
# Estimates y ~ x from CSV input, prints a model summary, and writes a ggplot2 figure.

args <- commandArgs(trailingOnly = TRUE)

usage <- function() {
  stop(
    "Usage: Rscript enhanced_linear_regression_r.R <filename> <x_column> <y_column> [output_png]",
    call. = FALSE
  )
}

if (length(args) < 3 || length(args) > 4) {
  usage()
}

filename <- args[[1]]
x_col <- args[[2]]
y_col <- args[[3]]
output_png <- if (length(args) == 4) args[[4]] else "enhanced_linear_regression_r_output.png"

if (!file.exists(filename)) {
  stop(sprintf("Input file not found: %s", filename), call. = FALSE)
}

data <- utils::read.csv(filename, stringsAsFactors = FALSE)

if (!(x_col %in% names(data)) || !(y_col %in% names(data))) {
  stop(
    sprintf(
      "Requested columns not present. Available columns: %s",
      paste(names(data), collapse = ", ")
    ),
    call. = FALSE
  )
}

formula <- stats::as.formula(paste(y_col, "~", x_col))
model <- stats::lm(formula, data = data)

if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2", repos = "https://cloud.r-project.org")
}
library(ggplot2)

# Prefer tidy evaluation over deprecated aes_string()
plot_obj <- ggplot(data, aes(x = .data[[x_col]], y = .data[[y_col]])) +
  geom_point(color = "#c0392b", alpha = 0.85) +
  geom_smooth(method = "lm", se = TRUE, color = "#2980b9", fill = "#AED6F1") +
  ggtitle(sprintf("%s as a function of %s", y_col, x_col)) +
  xlab(x_col) +
  ylab(y_col) +
  theme_minimal(base_size = 12)

ggsave(output_png, plot = plot_obj, width = 7.5, height = 5.0, dpi = 160)

cat(sprintf("Dataset: %s (n = %d)\n", filename, nrow(data)))
cat(sprintf("Specification: %s ~ %s\n", y_col, x_col))
print(summary(model))
cat(sprintf("Figure written to: %s\n", output_png))
