# 🎮 A/B Testing for User Engagement Analysis in Mobile Games

![Domain](https://img.shields.io/badge/Domain-Data%20Science%20%7C%20Analytics-blue)
![Tech](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas%20%7C%20SciPy-orange)
![Stats](https://img.shields.io/badge/Methods-A%2FB%20Testing%20%7C%20Hypothesis%20Testing-success)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Seaborn-purple)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 Project Overview

This project focuses on **data-driven decision making** through **A/B Testing** in the context of mobile gaming analytics.  
A synthetic experiment dataset was designed to evaluate the impact of a newly introduced game feature on **user engagement and monetization metrics**.

The analysis simulates real-world gameplay behavior by comparing a **control group** against a **test group**, measuring changes in session duration, user retention, and in-app purchases using **statistical hypothesis testing**.

---

## 🎯 Objective

To apply core **data science, statistics, and experimentation principles** by:

- Evaluating group-wise user engagement performance
- Visualizing behavioral patterns across cohorts
- Performing rigorous statistical hypothesis tests
- Deriving actionable product insights from data

---

## 🧪 Experimental Design & Dataset

A synthetic dataset was generated to emulate realistic mobile game user behavior with the following attributes:

- `user_id` – Unique player identifier  
- `group` – Experiment group (`control` / `test`)  
- `session_duration` – Average gameplay session duration (minutes)  
- `retention` – Binary indicator (1 = returned user, 0 = churned)  
- `in_app_purchases` – Total in-game spending (USD)  

---

## 📊 Statistical Analysis Pipeline

### 🔍 Descriptive & Exploratory Analysis
- Summary statistics to compare central tendencies and dispersion
- Distribution analysis of session duration and spending behavior

### 📈 Data Visualization
- **Boxplots** for session duration comparison
- **Bar charts** for retention and purchase rate analysis
- Visual validation of experiment assumptions

### 🧠 Hypothesis Testing
- **Independent T-Test** – Mean session duration comparison  
- **Chi-Square Test** – Retention rate significance  
- **Mann–Whitney U Test** – Non-parametric spending comparison  

---

### 📐 Statistical Equations & Methodology

This project applies multiple statistical hypothesis tests to validate experimental results and ensure reliable, data-driven conclusions.


---

#### 🔹 Independent Two-Sample T-Test (Session Duration)

-Used to compare the mean session duration between the control and test groups.

#### Null Hypothesis (H₀):
Mean session duration is equal for both groups.

#### Alternative Hypothesis (H₁):
Mean session duration differs between the groups.

## Test Statistic:

t = (X̄₁ − X̄₂) / √( (s₁² / n₁) + (s₂² / n₂) )


Where:

-X̄₁ , X̄₂ = sample means

-s₁² , s₂² = sample variances

-n₁ , n₂ = sample sizes

A statistically significant p-value (< 0.05) indicates a meaningful difference in session duration.


---

🔹 Chi-Square Test of Independence (User Retention)

Used to determine whether user retention is dependent on group assignment.

Null Hypothesis (H₀):
Retention is independent of group membership.

Alternative Hypothesis (H₁):
Retention depends on whether the user is in the control or test group.

Test Statistic:

χ² = Σ ( (O − E)² / E )


Where:

O = observed frequency

E = expected frequency

A significant chi-square value confirms an association between the feature and retention behavior.

🔹 Mann–Whitney U Test (In-App Purchases)

A non-parametric test used due to skewed spending distributions.

Null Hypothesis (H₀):
Both groups originate from the same distribution.

Alternative Hypothesis (H₁):
The spending distributions differ between groups.

Test Statistic:

U = n₁n₂ + (n₁(n₁ + 1))/2 − R₁


Where:

n₁ = sample size of group 1

R₁ = rank sum of group 1

This ensures robustness when normality assumptions are violated.

🔹 Significance Level

All statistical tests were evaluated at a 95% confidence level:

α = 0.05


p < α → Reject the null hypothesis

p ≥ α → Fail to reject the null hypothesis

🔹 Assumption Validation

Before hypothesis testing:

-Distribution symmetry and outliers were inspected using boxplots

-Sample independence was ensured by experimental design

-Non-parametric tests were applied when normality was not satisfied

### 💡 Why This Matters

-Applying multiple hypothesis tests improves:

-Statistical rigor

-Reliability of experimental conclusions

-Real-world alignment with industry A/B testing practices


---


## 📈 Results Summary

- **Session Duration:** Statistically significant increase in the test group  
- **Retention Rate:** Improved user retention with strong statistical confidence  
- **In-App Purchases:** Higher average spending observed in the test group  

---

## ✅ Conclusion

The experimental results indicate that the newly introduced game feature **positively impacts user engagement and monetization**.  
Findings support **broader feature rollout**, with recommendations for continued experimentation and long-term monitoring.

---

## 🛠️ Tools & Technologies

- **Programming Language:** Python  
- **Data Analysis:** Pandas, NumPy  
- **Statistical Testing:** SciPy  
- **Visualization:** Matplotlib, Seaborn  
- **Environment:** Jupyter Notebook  
- **Deployment (Planned):** Streamlit  

---

## 🚀 Deployment Plan

- Interactive dashboard using **Streamlit**
- Live visualization of metrics and statistical outcomes
- Deployment via **Streamlit Cloud** or **Render**

---

## 📂 Repository Structure


```
Data_Driven_Decisions/
│
├── ab_testing_game_analysis.py # Core analysis & statistical testing
├── synthetic_ab_test_dataset.csv # Synthetic experiment dataset
├── streamlit_app.py # Interactive dashboard (planned)
└── README.md # Project documentation

```


---

## 📚 Learning Outcomes

- Hands-on experience with **A/B Testing and experimental design**
- Practical application of **statistical hypothesis testing**
- Strong understanding of **user engagement analytics**
- Data visualization for **decision-making insights**
- End-to-end analytics workflow from data to product recommendation

---

## 👤 Author


**Priyanshu Aggarwal**  
Electronics & Communication Engineering  

📧 Email: Priyanshuaggarwal.in@gmail.com  
🔗 LinkedIn: https://linkedin.com/in/priyanshu1201  
💻 GitHub: https://github.com/AggarwalPriyanshu  

---

⭐ If you find this repository useful, feel free to star it!

