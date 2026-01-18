from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    qty: int = Field(gt=0)

class OrderCreate(BaseModel):
    items: List[OrderItemCreate] = Field(min_length=1)

class OrderItemOut(BaseModel):
    product_id: int
    qty: int
    unit_price: float
    line_total: float

    class Config:
        from_attributes = True

class OrderOut(BaseModel):
    id: int
    created_at: datetime
    total: float
    items: List[OrderItemOut]

    class Config:
        from_attributes = True

class OrderSummaryOut(BaseModel):
    id: int
    created_at: datetime
    total: float

    class Config:
        from_attributes = True

class PaginatedOrdersOut(BaseModel):
    items: list[OrderSummaryOut]
    total: int
    limit: int
    offset: int