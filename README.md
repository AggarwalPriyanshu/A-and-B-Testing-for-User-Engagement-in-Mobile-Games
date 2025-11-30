# Data_Driven_Decisions

# A/B Testing for User Engagement Analysis in Mobile Games

## 📌 Overview

This project analyzes a synthetic A/B testing dataset designed to evaluate the impact of a new game feature on user engagement metrics like session duration, retention, and in-app purchases. The experiment simulates real-world gameplay behavior and compares a control group with a test group.

## 🎯 Objective

To apply core data science and hypothesis testing principles in a gaming context by:

- Analyzing group-wise performance
- Visualizing user behavior
- Performing rigorous statistical testing
- Drawing actionable insights

## 📊 Dataset

A synthetic dataset was generated with the following features:

- `user_id`: Unique identifier
- `group`: Either "control" or "test"
- `session_duration`: Average play session length in minutes
- `retention`: Binary indicator (1 if the user returned, 0 otherwise)
- `in_app_purchases`: Amount spent in-game (in USD)

## 🔍 Key Analysis

- **Descriptive statistics** to summarize user behavior.
- **Boxplots** and **bar charts** for visual comparison.
- **T-test**, **Chi-square test**, and **Mann-Whitney U test** to test hypotheses.

## 📈 Results Summary

- **Session Duration**: Increased significantly in the test group.
- **Retention**: Improved in the test group with statistical significance.
- **In-App Purchases**: Test group showed higher average spending.

## ✅ Conclusion

The new feature led to notable improvements across all key metrics. The results support broader implementation with continued monitoring.

## 🛠️ Tech Stack

- Python (Pandas, Matplotlib, Seaborn, Scipy)
- Jupyter Notebook
- Streamlit (for frontend)

## 🚀 Deployment

Streamlit app coming soon to visualize and interact with the dataset and statistical results.

## 📂 File Structure

```
├── ab_testing_game_analysis.py
├── synthetic_ab_test_dataset.csv
├── README.md
├── streamlit_app.py (to be added)
```

## 🙋‍♂️ Author

**Sanat Walia** – BTech CSE Student, Passionate about data science, gaming analytics, and deploying data-driven solutions.

## 🌐 Live Demo

🚧 _To be deployed using Streamlit Cloud or Render_ 🚧
