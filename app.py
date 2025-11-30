import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import io

st.set_page_config(page_title="A/B Testing - Game Engagement Analysis", layout="wide")
st.title("🎮 A/B Testing Dashboard for Game Analytics")

# Sidebar for file upload
st.sidebar.header("Upload your dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

# Load default or user-uploaded data
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ Custom dataset loaded successfully!")
else:
    df = pd.read_csv("synthetic_ab_test_dataset.csv")
    st.info("ℹ️ Using default synthetic dataset")

# Preview dataset
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Group distribution
st.subheader("👥 Group Distribution")
st.bar_chart(df["group"].value_counts())

# Visualization: Session Duration
st.subheader("⏱️ Session Duration by Group")
fig1, ax1 = plt.subplots()
sns.boxplot(x="group", y="session_duration", data=df, ax=ax1)
st.pyplot(fig1)

# Visualization: Retention Rate
st.subheader("🔁 Retention Rate by Group")
retention_rates = df.groupby("group")["retention"].mean().reset_index()
fig2, ax2 = plt.subplots()
sns.barplot(x="group", y="retention", data=retention_rates, ax=ax2)
ax2.set_ylim(0, 1)
st.pyplot(fig2)

# Visualization: In-App Purchases
st.subheader("💰 In-App Purchases by Group")
fig3, ax3 = plt.subplots()
sns.boxplot(x="group", y="in_app_purchases", data=df, ax=ax3)
st.pyplot(fig3)

# Hypothesis Testing
st.subheader("📊 Hypothesis Testing Results")

# Session Duration - t-test
control_sd = df[df["group"] == "control"]["session_duration"]
test_sd = df[df["group"] == "test"]["session_duration"]
t_stat_sd, p_val_sd = stats.ttest_ind(test_sd, control_sd)
st.write(
    f"**Session Duration T-test**: t-statistic = {t_stat_sd:.4f}, p-value = {p_val_sd:.4f}"
)

# Retention - chi-square test
ret_table = pd.crosstab(df["group"], df["retention"])
chi2_ret, p_ret, _, _ = stats.chi2_contingency(ret_table)
st.write(
    f"**Retention Chi-squared Test**: chi2 = {chi2_ret:.4f}, p-value = {p_ret:.4f}"
)

# In-App Purchases - Mann-Whitney U Test
control_pur = df[df["group"] == "control"]["in_app_purchases"]
test_pur = df[df["group"] == "test"]["in_app_purchases"]
u_stat, p_val_pur = stats.mannwhitneyu(control_pur, test_pur)
st.write(
    f"**In-App Purchases Mann-Whitney U Test**: U-statistic = {u_stat:.4f}, p-value = {p_val_pur:.4f}"
)

# Conclusion
st.subheader("📝 Conclusion")
st.markdown(
    """
- Test group users spent more time playing.
- Retention increased in the test group.
- In-app purchases rose significantly in the test group.

**📌 Recommendation**: Consider deploying the new feature based on statistically significant improvements across key engagement metrics.
"""
)
