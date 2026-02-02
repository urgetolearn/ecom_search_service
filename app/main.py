from fastapi import FastAPI
from app.api.v1.routes import router
from app.services.catalog import catalog_service
import pandas as pd

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Force data into memory on startup
    df = pd.read_csv("gadgets.csv")
    for _, row in df.iterrows():
        catalog_service.add_product({
            "title": row['Product_Name'],
            "price": float(row['Price']),
            "mrp": float(row['Price'] * 1.2), # Synthetic MRP
            "rating": float(row.get('Rating', 0)),
            "stock": 10,
            "description": row.get('Description', '')
        })
    print(f"startup Complete: {len(catalog_service.products)} items loaded.")

app.include_router(router)