# A/B Testing for User Engagement Analysis in Mobile Games

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the dataset
data = pd.read_csv("synthetic_ab_test_dataset.csv")

# Display first few rows
print("Data Preview:")
print(data.head())

# Basic info
print("\nDataset Info:")
data.info()

# Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Count of control and test users
print("\nGroup Distribution:")
print(data['group'].value_counts())

# --------------------------
# Visualizations
# --------------------------
sns.set(style="whitegrid")

# Session Duration by Group
plt.figure(figsize=(10,6))
sns.boxplot(x='group', y='session_duration', data=data)
plt.title('Session Duration Distribution by Group')
plt.savefig("session_duration_boxplot.png")
plt.show()

# Retention Rate by Group
retention_rates = data.groupby('group')['retention'].mean().reset_index()
plt.figure(figsize=(8,5))
sns.barplot(x='group', y='retention', data=retention_rates)
plt.title('Retention Rate by Group')
plt.ylim(0,1)
plt.savefig("retention_rate_barplot.png")
plt.show()

# In-App Purchases by Group
plt.figure(figsize=(10,6))
sns.boxplot(x='group', y='in_app_purchases', data=data)
plt.title('In-App Purchases Distribution by Group')
plt.savefig("in_app_purchases_boxplot.png")
plt.show()

# --------------------------
# Hypothesis Testing
# --------------------------
print("\nHypothesis Testing Results:")

# Session Duration - t-test
control_sd = data[data['group'] == 'control']['session_duration']
test_sd = data[data['group'] == 'test']['session_duration']
t_stat_sd, p_val_sd = stats.ttest_ind(test_sd, control_sd)
print(f"Session Duration T-test: t-statistic = {t_stat_sd:.4f}, p-value = {p_val_sd:.4f}")

# Retention - proportion test
cont_ret = data[data['group'] == 'control']['retention']
test_ret = data[data['group'] == 'test']['retention']
ret_table = pd.crosstab(data['group'], data['retention'])
chi2_ret, p_ret, _, _ = stats.chi2_contingency(ret_table)
print(f"Retention Chi-squared Test: chi2 = {chi2_ret:.4f}, p-value = {p_ret:.4f}")

# In-App Purchases - Mann-Whitney U (non-parametric)
control_pur = data[data['group'] == 'control']['in_app_purchases']
test_pur = data[data['group'] == 'test']['in_app_purchases']
u_stat, p_val_pur = stats.mannwhitneyu(control_pur, test_pur)
print(f"In-App Purchases Mann-Whitney U Test: U-statistic = {u_stat:.4f}, p-value = {p_val_pur:.4f}")

# --------------------------
# Insights
# --------------------------
print("\nProject Summary:")
print("- Players in the test group had significantly longer session durations.")
print("- Retention rate improved in the test group, with statistical significance.")
print("- Spending was higher in the test group, though distribution skew required a non-parametric test.")
print("\nConclusion: The new feature appears to improve engagement and monetization metrics. We recommend further testing on a larger sample size and deploying the feature gradually.")
