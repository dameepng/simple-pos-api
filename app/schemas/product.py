from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    sku: str = Field(min_length=1, max_length=64)
    name: str = Field(min_length=1, max_length=255)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)

class ProductOut(BaseModel):
    id: int
    sku: str
    name: str
    price: float
    stock: int

    class Config:
        from_attributes = True

class StockUpdate(BaseModel):
    stock: int = Field(ge=0)