import streamlit as st
import pandas as pd

st.set_page_config(page_title="E-Commerce Price Intelligence", layout="wide")

DATA_PATH = "data/cleaned_data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["extracted_at"] = pd.to_datetime(df["extracted_at"])
    return df

df = load_data()

st.title("📊 E-Commerce Price Intelligence Dashboard")

# KPI Section
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Records Tracked", len(df))

with col2:
    st.metric("Average Price", round(df["price"].mean(), 2))

st.divider()

# Trend Analysis
st.subheader("Price Trend Over Time")

trend_df = df.groupby("extracted_at")["price"].mean().reset_index()
st.line_chart(trend_df.set_index("extracted_at"))

st.divider()

# Category Analysis
st.subheader("Category-wise Average Price")

category_df = df.groupby("category")["price"].mean().reset_index()
st.bar_chart(category_df.set_index("category"))
