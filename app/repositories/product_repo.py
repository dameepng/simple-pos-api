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

    def update_stock(self, db, product, new_stock: int):
        product.stock = new_stock
        db.flush()
        return product

    def get_for_update(self, db, product_id: int) -> Product | None:
        """
        Row-lock product untuk transaksi (PostgreSQL).
        SQLite fallback: behave like normal SELECT.
        """
        stmt = select(Product).where(Product.id == product_id)

        # hanya aktifkan FOR UPDATE kalau DB mendukung (PostgreSQL)
        if db.bind and db.bind.dialect.name in {"postgresql", "mysql"}:
            stmt = stmt.with_for_update()

        return db.execute(stmt).scalar_one_or_none()
