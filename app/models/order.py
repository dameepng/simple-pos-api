from datetime import datetime
from sqlalchemy import Integer, DateTime, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    total: Mapped[float] = mapped_column(Numeric(12, 2), default=0)

    items = relationship(
        "OrderItem",
        back_populates="order",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

