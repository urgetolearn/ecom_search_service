from pydantic import BaseModel
from typing import Dict, Optional

class ProductCreate(BaseModel):
    title: str
    description: str
    rating: float
    stock: int
    price: float
    mrp: float
    currency: str = "Rupee"

class ProductMetaUpdate(BaseModel):
    productId: int
    Metadata: Dict[str, str]
