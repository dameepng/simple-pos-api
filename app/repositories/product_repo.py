from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product

class ProductRepository:
    def get_by_sku(self, db: Session, sku: str) -> Product | None:
        stmt = select(Product).where(Product.sku == sku)
        return db.execute(stmt).scalar_one_or_none()

    def get(self, db: Session, product_id: int) -> Product | None:
        return db.get(Product, product_id)

    def list(self, db: Session, limit: int = 50, offset: int = 0) -> list[Product]:
        stmt = select(Product).order_by(Product.id.desc()).limit(limit).offset(offset)
        return list(db.execute(stmt).scalars())

    def create(self, db: Session, *, sku: str, name: str, price: float, stock: int) -> Product:
        p = Product(sku=sku, name=name, price=price, stock=stock)
        db.add(p)
        db.flush()   # biar dapat id tanpa commit
        return p
