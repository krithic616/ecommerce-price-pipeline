import pandas as pd
from datetime import datetime
import random

def fetch_data():
    products = [
        {"product": "Laptop", "category": "electronics"},
        {"product": "Gold Ring", "category": "jewelry"},
        {"product": "T-Shirt", "category": "men's clothing"},
        {"product": "Dress", "category": "women's clothing"},
    ]

    data = []

    for item in products:
        price = round(random.uniform(20, 500), 2)
        data.append({
            "product": item["product"],
            "category": item["category"],
            "price": price,
            "extracted_at": datetime.now()
        })

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = fetch_data()
    df.to_csv("data/raw_data.csv", index=False)
    print("Raw data saved successfully.")
