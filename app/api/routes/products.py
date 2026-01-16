from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.product import ProductCreate, ProductOut, StockUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["products"])
svc = ProductService()

@router.post("", response_model=ProductOut, status_code=201)
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):
    with db.begin():  # transaksi
        p = svc.create_product(db, **payload.model_dump())
    return p

@router.get("", response_model=list[ProductOut])
def list_products(limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return svc.list_products(db, limit=limit, offset=offset)

@router.patch("/{product_id}/stock", response_model=ProductOut)
def update_stock(product_id: int, payload: StockUpdate, db: Session = Depends(get_db)):
    with db.begin():
        p = svc.update_stock(db, product_id=product_id, stock=payload.stock)
    return p