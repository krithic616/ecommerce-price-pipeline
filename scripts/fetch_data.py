import requests
import pandas as pd
from datetime import datetime

def fetch_data():
    url = "https://fakestoreapi.com/products"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

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
