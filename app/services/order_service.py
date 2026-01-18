from fastapi import HTTPException
from sqlalchemy.orm import Session

from collections import defaultdict
from app.repositories.order_repo import OrderRepository
from app.repositories.product_repo import ProductRepository
from app.models.order_item import OrderItem

class OrderService:
    def __init__(self) -> None:
        self.orders = OrderRepository()
        self.products = ProductRepository()

    def create_order(self, db: Session, *, items: list[dict]):
        # merge duplicate product_id
        merged: dict[int, int] = defaultdict(int)
        for it in items:
            merged[int(it["product_id"])] += int(it["qty"])

        normalized_items = [
            {"product_id": pid, "qty": qty}
            for pid, qty in merged.items()
        ]

        order = self.orders.create(db)
        total = 0.0

        for item in normalized_items:
            product = self.products.get_for_update(db, item["product_id"])
            if not product:
                raise HTTPException(404, f"Product {item['product_id']} not found")

            if product.stock < item["qty"]:
                raise HTTPException(400, f"Insufficient stock for product {product.id}")

            unit_price = float(product.price)
            line_total = unit_price * item["qty"]
            total += line_total

            product.stock -= item["qty"]

            db.add(OrderItem(
                order_id=order.id,
                product_id=product.id,
                qty=item["qty"],
                unit_price=unit_price,
                line_total=line_total,
            ))

        order.total = total
        db.flush()

        return self.orders.get(db, order.id)

