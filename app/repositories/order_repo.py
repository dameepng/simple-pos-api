from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.order import Order

class OrderRepository:
    def create(self, db: Session) -> Order:
        order = Order()
        db.add(order)
        db.flush()
        return order

    def get(self, db: Session, order_id: int) -> Order | None:
        stmt = (
            select(Order)
            .options(selectinload(Order.items))
            .where(Order.id == order_id)
        )
        return db.execute(stmt).scalar_one_or_none()

    def list(self, db: Session, limit: int = 50, offset: int = 0) -> list[Order]:
        stmt = (
            select(Order)
            .order_by(Order.id.desc())
            .limit(limit)
            .offset(offset)
        )
        return list(db.execute(stmt).scalars())
