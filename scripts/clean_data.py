import pandas as pd
import os

RAW_PATH = "data/raw_data.csv"
CLEAN_PATH = "data/cleaned_data.csv"

def clean_data():
    if not os.path.exists(RAW_PATH):
        raise Exception("Raw data file not found.")

    df = pd.read_csv(RAW_PATH)

    df = df.drop_duplicates()
    df = df.dropna()

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    return df

def append_historical_data(df):
    if os.path.exists(CLEAN_PATH):
        existing_df = pd.read_csv(CLEAN_PATH)
        df = pd.concat([existing_df, df], ignore_index=True)

    df.to_csv(CLEAN_PATH, index=False)
    print("Cleaned data saved and history updated.")

if __name__ == "__main__":
    df = clean_data()
    append_historical_data(df)
