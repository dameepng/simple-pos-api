from pydantic import BaseModel, Field, ConfigDict
from decimal import Decimal

class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=64)
    name: str = Field(min_length=1, max_length=255)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    sku: str
    name: str
    price: Decimal
    stock: int

class StockUpdate(BaseModel):
    stock: int = Field(ge=0)