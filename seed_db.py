import pandas as pd
import requests
import json

# Configuration
CSV_PATH = "gadgets.csv"
API_URL = "http://127.0.0.1:8000/api/v1/product"

def load_and_push():
    try:
        df = pd.read_csv(CSV_PATH)

        df['Price'] = df['Price'].fillna(0)
        df['Rating'] = df['Rating'].fillna(0)
        print(f"Successfully loaded {len(df)} rows from {CSV_PATH}")

        subset = df.head(1000)

        for index, row in subset.iterrows():
            payload = {
                "title": str(row.get('Product_Name', 'Unknown Gadget')),
                "description": f"Category: {row.get('Category', 'Electronics')}. Rating based on {row.get('Number_of_Ratings', 0)} users.",
                "rating": float(row.get('Rating', 0)),
                "stock": 50, 
                "price": float(row.get('Price', 0)),
                "mrp": float(row.get('Price', 0) * 1.25), 
                "currency": "Rupee"
            }
            requests.post(API_URL, json=payload)
            if index % 100 == 0:
                print(f"Processed {index} rows...")

        print("Database seeding complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    load_and_push()