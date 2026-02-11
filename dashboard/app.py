import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="E-Commerce Price Dashboard", layout="wide")

st.title("📊 E-Commerce Price Monitoring Dashboard")

# GitHub raw CSV URL
DATA_URL = "https://raw.githubusercontent.com/krithic616/ecommerce-price-pipeline/main/data/cleaned_data.csv"

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df

df = load_data()

# Convert extracted_at column to datetime
df["extracted_at"] = pd.to_datetime(df["extracted_at"])

# Last updated timestamp
last_updated = df["extracted_at"].max()

st.markdown(f"### 🕒 Last Updated: {last_updated.strftime('%d %b %Y - %I:%M %p')}")

st.divider()

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(df))
col2.metric("Average Price", f"${df['price'].mean():.2f}")
col3.metric("Max Price", f"${df['price'].max():.2f}")

st.divider()

st.subheader("Price Distribution")

st.bar_chart(df.groupby("category")["price"].mean())
