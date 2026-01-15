from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.product_repo import ProductRepository

class ProductService:
    def __init__(self) -> None:
        self.repo = ProductRepository()

    def create_product(self, db: Session, *, sku: str, name: str, price: float, stock: int):
        if self.repo.get_by_sku(db, sku):
            raise HTTPException(status_code=409, detail="SKU already exists")
        return self.repo.create(db, sku=sku, name=name, price=price, stock=stock)

    def list_products(self, db: Session, limit: int, offset: int):
        return self.repo.list(db, limit=limit, offset=offset)
