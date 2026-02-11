import requests
import pandas as pd
from datetime import datetime

# API endpoint
URL = "https://fakestoreapi.com/products"

def fetch_data():
    response = requests.get(URL)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    data = response.json()
    df = pd.DataFrame(data)

    # Add extraction timestamp
    df["extracted_at"] = datetime.now()

    return df

def save_raw_data(df):
    df.to_csv("data/raw_data.csv", index=False)
    print("Raw data saved successfully.")

if __name__ == "__main__":
    df = fetch_data()
    save_raw_data(df)
