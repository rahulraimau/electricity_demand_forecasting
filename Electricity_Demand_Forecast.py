import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64 # For embedding the image

# --- Data and Results (Hardcoded from the analysis report for demonstration) ---
# In a real application, these would be loaded from saved models/data files.

# Error Metrics
error_metrics_data = {
    'Model': ['Decomposition', 'Exponential Smoothing', 'SARIMA'],
    'RMSE': [5.392, 3.549, 3.671],
    'MAPE (%)': [4.419, 2.566, 2.570],
    'RMSPE (%)': [5.073, 3.666, 3.711]
}
error_metrics_df = pd.DataFrame(error_metrics_data)

# Selected Model and Justification
selected_model_name = "Exponential Smoothing"
reason_for_selection = "The Exponential Smoothing model exhibited the lowest RMSE (3.549) among all evaluated models. A lower RMSE indicates that the model's predictions are, on average, closer to the actual values, signifying higher accuracy and better fit to the underlying patterns in the electricity consumption data. While MAPE and RMSPE were also competitive, RMSE served as the primary selection criterion for its direct measure of prediction error magnitude."

# Demand Estimation for next 1-2 years (January 2020 to December 2021)
demand_estimation_data = {
    'Date': pd.to_datetime([
        '2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01',
        '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01',
        '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01',
        '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01'
    ]),
    'Electricity Consumption (Trillion Watts)': [
        109.106, 102.298, 95.507, 89.625, 94.756, 109.989,
        120.495, 120.016, 107.418, 94.241, 92.707, 102.681,
        110.611, 103.802, 97.011, 91.129, 96.261, 111.494,
        122.000, 121.521, 108.923, 95.746, 94.212, 104.185
    ]
}
demand_estimation_df = pd.DataFrame(demand_estimation_data)
demand_estimation_df['Date'] = demand_estimation_df['Date'].dt.strftime('%Y-%m-%d') # Format date for display

# --- Streamlit App Layout ---

st.set_page_config(layout="wide") # Use wide layout

st.title("⚡ Electricity Demand Forecasting Report")

st.markdown("""
This report provides an overview of the electricity demand forecasting analysis,
including the methodology, model performance, and future demand estimations.
""")

st.header("1. Methodology")
st.markdown("""
The forecasting process involved:
-   **Data Preprocessing:** Loading `Electricity Consumption.csv`, converting 'DATE' to datetime, and setting it as the index.
-   **Data Splitting:** Dividing data into training (Jan 1973 - Dec 2017) and testing (Jan 2018 - Dec 2019) sets for model validation.
-   **Model Implementation:** Comparing Decomposition, Exponential Smoothing (Holt-Winters), and SARIMA models.
-   **Error Metrics:** Evaluating models using RMSE, MAPE, and RMSPE.
""")

st.header("2. Results and Model Comparison")
st.markdown("The error metrics calculated for each model on the test data are as follows:")
st.table(error_metrics_df)

st.header("3. Selected Model and Justification")
st.markdown(f"Based on the evaluation metrics, the **{selected_model_name} Model** was selected as the best-performing model for forecasting electricity demand.")
st.markdown(f"**Reason for Selection:** {reason_for_selection}")

st.header("4. Demand Estimation for Next 1-2 Years")
st.markdown("Using the selected Exponential Smoothing model, the monthly electricity demand for the next 1-2 years (January 2020 to December 2021) is estimated:")
st.table(demand_estimation_df)

st.header("5. Visualization of Forecasts")
st.markdown("The following plot visualizes the historical data, actual test data, and the forecasts from all models.")

# To display the plot, you would typically save the plot from the Python script
# and then load it here. Assuming 'electricity_consumption_forecast.png' is available.
try:
    with open("electricity_consumption_forecast.png", "rb") as f:
        img_bytes = f.read()
        encoded_img = base64.b64encode(img_bytes).decode()
    st.image(f"data:image/png;base64,{encoded_img}", caption="Electricity Consumption Forecast (1-2 Years)", use_column_width=True)
except FileNotFoundError:
    st.warning("Forecast plot image 'electricity_consumption_forecast.png' not found. Please run the forecasting script to generate it.")
    # Fallback if image is not found (e.g., generate a dummy plot or skip)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.text(0.5, 0.5, "Plot not available.\nRun the forecasting script to generate the image.",
            horizontalalignment='center', verticalalignment='center', transform=ax.transAxes, fontsize=14, color='red')
    ax.set_title("Placeholder Plot")
    st.pyplot(fig)


st.header("6. Conclusion")
st.markdown("""
The Exponential Smoothing model provides reliable monthly forecasts for electricity demand for the next two years.
These estimations can be valuable for strategic planning, resource allocation, and operational management of electricity production to meet anticipated demand.
Further refinements could include incorporating external factors (e.g., temperature, economic indicators) and exploring more advanced models or ensemble methods for even greater accuracy.
""")