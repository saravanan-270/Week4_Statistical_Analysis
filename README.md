# Week 4 — Statistical Analysis and Hypothesis Testing

This project statistically validates key findings from Weeks 1–3 using the cleaned Gapminder dataset.

## Tests
1. Welch independent-samples t-test — Africa vs Europe life expectancy in 2007
2. Pearson correlation — GDP per capita vs life expectancy in 2007
3. OLS regression — life expectancy vs log GDP per capita
4. Chi-square test of independence — continent vs GDP-based development group

## Included
- data/gapminder_cleaned.csv
- data/analysis_2007.csv
- notebook/week4_statistical_analysis.ipynb
- scripts/statistical_analysis.py
- outputs/statistical_test_summary.csv
- outputs/assumption_checks.csv
- outputs/chi_square_contingency_table.csv
- report/Week_4_Statistical_Analysis_Report.docx
- requirements.txt

## Statistical practice
The report includes null/alternative hypotheses, test selection, assumptions, p-values, confidence intervals, effect sizes, regression diagnostics, and a Bonferroni sensitivity threshold of 0.0125.

## Source
Gapminder: https://www.gapminder.org/data/
Dataset documentation: https://jennybc.github.io/gapminder/reference/gapminder.html
