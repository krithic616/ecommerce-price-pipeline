import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="E-Commerce Price Dashboard", layout="wide")

st.title("📊 E-Commerce Price Monitoring Dashboard")


DATA_URL = "https://raw.githubusercontent.com/krithic616/ecommerce-price-pipeline/main/data/cleaned_data.csv"


@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    return df

df = load_data()


df["extracted_at"] = pd.to_datetime(df["extracted_at"])


last_updated = df["extracted_at"].max()

st.markdown(f"### 🕒 Last Updated: {last_updated.strftime('%d %b %Y - %I:%M %p')}")

st.divider()


col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(df))
col2.metric("Average Price", f"${df['price'].mean():.2f}")
col3.metric("Max Price", f"${df['price'].max():.2f}")

st.divider()

st.subheader("Price Distribution")

st.bar_chart(df.groupby("category")["price"].mean())
