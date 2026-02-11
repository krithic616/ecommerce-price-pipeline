import requests
import pandas as pd
from datetime import datetime
import time

def fetch_data():
    url = "https://fakestoreapi.com/products"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json",
        "Connection": "keep-alive"
    }

    # small delay to avoid bot detection
    time.sleep(2)

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    data = response.json()

    df = pd.DataFrame(data)
    df["extracted_at"] = datetime.now()

    return df


if __name__ == "__main__":
    df = fetch_data()
    df.to_csv("data/raw_data.csv", index=False)
    print("Raw data saved successfully.")
