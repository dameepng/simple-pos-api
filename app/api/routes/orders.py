from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.order import OrderCreate, OrderOut, OrderSummaryOut
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])
svc = OrderService()

@router.post("", response_model=OrderOut, status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    with db.begin():
        order = svc.create_order(db, items=[i.model_dump() for i in payload.items])
    return order

@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = svc.orders.get(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return order

# ✅ LIST orders + pagination
@router.get("", response_model=list[OrderSummaryOut])
def list_orders(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
):
    return svc.orders.list(db, limit=limit, offset=offset)
