# End-to-end-ML-project

\# CUSTOMER CHURN PREDICTION:-



This project aims to predict customer churn based on various attributes using supervised machine learning models. It includes exploratory data analysis, model building, evaluation, and deployment using Flask.



\## Problem Statement:



Telecom companies often lose a portion of their customers due to churn. By predicting which customers are likely to churn, businesses can take proactive steps to retain them. This project develops a machine learning model that predicts whether a customer will churn based on demographic and service-related features.



\##  Tech Stack



\- \*\*Languages\*\*: Python  

\- \*\*Libraries\*\*: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  

\- \*\*Modeling\*\*: Logistic Regression, Decision Tree, Random Forest  

\- \*\*Deployment\*\*: Flask  

\- \*\*Tools\*\*: Jupyter Notebook, Git, GitHub



\##  Project Structure:-



\##  Exploratory Data Analysis (EDA):



\- Distribution of churned vs non-churned customers

\- Impact of categorical variables (like contract type, tenure, internet service)

\- Correlation heatmaps

\- Outlier detection and value counts



\##  Machine Learning Models

| Model               | Accuracy | Precision | Recall | F1-score |
|--------------------|----------|-----------|--------|----------|
| Logistic Regression| 85%      | 84%       | 85%    | 84%      |
| Decision Tree      | 88%      | 87%       | 88%    | 87%      |
| Random Forest      | 94%      | 94%       | 94%    | 94%      |



>  Random Forest was selected as the best-performing model.



\##  Web App Demo:



\- Built using \*\*Flask\*\*

\- Takes user inputs (gender, tenure, contract type, etc.)

\- Predicts churn probability in real-time

\- Simple and clean HTML interface using Flask templates



