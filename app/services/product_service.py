from fastapi import HTTPException
from sqlalchemy.orm import Session
from decimal import Decimal

from app.repositories.product_repo import ProductRepository
from app.core.money import to_decimal, quantize_money

class ProductService:
    def __init__(self) -> None:
        self.repo = ProductRepository()

    def create_product(self, db: Session, *, sku: str, name: str, price: Decimal, stock: int):
        if self.repo.get_by_sku(db, sku):
            raise HTTPException(status_code=409, detail="SKU already exists")
        price_dec = quantize_money(to_decimal(price))
        return self.repo.create(db, sku=sku, name=name, price=price_dec, stock=stock)

    def list_products(self, db: Session, limit: int, offset: int):
        return self.repo.list(db, limit=limit, offset=offset)

    def update_stock(self, db, *, product_id: int, stock: int):
        product = self.repo.get(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return self.repo.update_stock(db, product, stock)
