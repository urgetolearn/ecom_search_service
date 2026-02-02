from fastapi import APIRouter, HTTPException
from app.models.product import ProductCreate, ProductMetaUpdate
from app.services.catalog import catalog_service

router = APIRouter(prefix="/api/v1")

@router.post("/product")
def create_product(product: ProductCreate):
    product_id = catalog_service.add_product(product.dict())
    return {"productId": product_id}


@router.put("/product/meta-data")
def update_metadata(data: ProductMetaUpdate):
    updated = catalog_service.update_metadata(
        data.productId, data.Metadata
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return {
        "productId": data.productId,
        "Metadata": updated["Metadata"]
    }


@router.get("/search/product")
def search_product(query: str):
    results = catalog_service.search(query)

    return {
        "data": [
            {
                "productId": p["productId"],
                "title": p["title"],
                "description": p["description"],
                "mrp": p["mrp"],
                "Sellingprice": p["price"],
                "Metadata": p["Metadata"],
                "stock": p["stock"]
            }
            for p in results
        ]
    }
