import streamlit as st
import pandas as pd
import joblib

# Load models
kmeans = joblib.load("outputs/models/K-Means_model.pkl")
scaler = joblib.load("outputs/Scaler")

# Define cluster labels (adjust after checking centroids)
cluster_labels = {
    0: "Premium Customers (High Income, High Spending)",
    1: "Careful Customers (Low Income, Low Spending)",
    2: "Cautious Customers (High Income, Low Spending)",
    3: "Impulsive Customers (Low Income, High Spending)"
}


st.title("Customer Segmentation App")

st.image("data/raw/custemer segmentation.png", caption="Customer Segmentation", use_container_width=True)

st.subheader(" Customer Segments Explanation")
st.write("""
- **Low Income, Low Spending → "Careful Customers"**  
  Don’t spend much, low income. Small target group.

- **Low Income, High Spending → "Impulsive Customers"**  
  Spend a lot relative to income. Could be risky but also high opportunity.

- **High Income, Low Spending → "Cautious Customers"**  
  Have money but don’t spend much. Need better engagement.

- **High Income, High Spending → "Premium Customers"**  
  High spenders with high income. Best customers (loyalty programs, premium offers).
""")

st.sidebar.subheader(" Predict Your Segment")
st.sidebar.write("Enter your information to be assigned to a Customers cluster:")

# User input
Spending_Score = st.sidebar.number_input("Spending Score (1-100)", min_value=1, max_value=99, value=50)
Annual_Income = st.sidebar.number_input("Annual Income (k$)", min_value=15, max_value=137, value=60)

# convert to dataframe
df = pd.DataFrame({
    "Annual Income (k$)": [Annual_Income],
    "Spending Score (1-100)": [Spending_Score]
})

# Scale input data
scaled_df = scaler.transform(df)

# Prediction
if st.sidebar.button("Predict Segment"):
    cluster = kmeans.predict(scaled_df)[0]
    label = cluster_labels[cluster]
    st.success(f"Predicted Segment: {label}")
