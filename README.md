⚡ Electricity Demand Estimation – Time Series Forecasting Project
📌 Project Overview
This capstone project focuses on building a robust time series model to estimate monthly electricity demand for a leading power distribution company. With data from 1973 to 2019, the goal is to forecast demand for the next 1–2 years to help in efficient production planning and vendor management.

🎯 Business Objective
🔮 Forecast electricity consumption on a monthly basis for the next 1–2 years.

📉 Evaluate forecasting accuracy using RMSE, RMSPE, and MAPE.

🔍 Compare multiple time series models:

Trend decomposition

Exponential Smoothing (ETS)

ARIMA/SARIMA

✅ Select the best-performing model and explain the rationale.

📁 Dataset Description
Source: Historical consumption data (internal)

Time Range: January 1973 – December 2019

Frequency: Monthly

Features:

Column	Description
Date	Month and Year of observation
Electricity_Consumption	Electricity demand (in Trillion Watts)

🧪 Techniques & Tools Used
Language: Python

Key Libraries: pandas, numpy, matplotlib, statsmodels, pmdarima, seaborn

Models Applied:

Classical Decomposition Models

ETS (Error, Trend, Seasonality) models

ARIMA and SARIMA with grid search tuning

Evaluation Metrics:

RMSE – Root Mean Squared Error

MAPE – Mean Absolute Percentage Error

RMSPE – Root Mean Square Percentage Error

🚀 How to Run
Clone the repo:

bash
Copy
Edit
git clone https://github.com/rahulraimau/electricity-demand-estimation.git
cd electricity-demand-estimation
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the notebook:

bash
Copy
Edit
jupyter notebook demand_forecasting.ipynb
📈 Sample Visuals
Line plot of historical demand (1973–2019)

Seasonal Decomposition plots (Trend, Seasonality, Residual)

Forecast plot with confidence intervals

Error metric comparison across models

📦 Output Deliverables
📊 Final forecast for Jan 2020 – Dec 2021

📁 forecast_results.csv – containing monthly predictions

📉 model_metrics.json – RMSE, MAPE, RMSPE for all models

📌 Best Model: SARIMA (example) – selected based on lowest MAPE

✅ Key Takeaways
SARIMA model produced the most accurate forecasts due to its ability to model seasonality effectively.

Capturing historical seasonality is critical in electricity consumption modeling.

Time series validation was done using train-test split on last 24 months.

👤 Author
Rahul Rai
📧 rahulraimau5@gmail.com
🔗 GitHub | Kaggle | LinkedIn

