from pydantic import BaseModel, Field, ConfigDict
from typing import List
from datetime import datetime

class OrderItemCreate(BaseModel):
    product_id: int
    qty: int = Field(gt=0)

class OrderCreate(BaseModel):
    items: List[OrderItemCreate] = Field(min_length=1)

class OrderItemOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    product_id: int
    qty: int
    unit_price: float
    line_total: float

class OrderOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    total: float
    items: List[OrderItemOut]

class OrderSummaryOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime
    total: float

class PaginatedOrdersOut(BaseModel):
    items: list[OrderSummaryOut]
    total: int
    limit: int
    offset: int