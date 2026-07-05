import streamlit as st
import pandas as pd
from src.predict import predict

st.title("Public Transport Analytics Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Drop passengers column if present
    if "passengers" in df.columns:
        df = df.drop(columns=["passengers"])

    st.write("Input Data", df)

    preds = predict(df)
    st.write("Predictions", preds)
