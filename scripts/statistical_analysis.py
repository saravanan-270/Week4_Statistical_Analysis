import pandas as pd
from scipy import stats
import statsmodels.api as sm

df = pd.read_csv("data/gapminder_cleaned.csv")
d = df[df["year"] == 2007].copy()

# Welch t-test
af = d.loc[d["continent"]=="Africa","lifeexp"]
eu = d.loc[d["continent"]=="Europe","lifeexp"]
print("Welch t-test:", stats.ttest_ind(af, eu, equal_var=False))

# Pearson correlation
print("Pearson:", stats.pearsonr(d["gdp_per_capita"], d["lifeexp"]))

# OLS
X = sm.add_constant(d["log_gdp_per_capita"])
model = sm.OLS(d["lifeexp"], X).fit()
print(model.summary())

# Chi-square
table = pd.crosstab(d["continent"], d["development_group"])
print("Chi-square:", stats.chi2_contingency(table))
print(table)
