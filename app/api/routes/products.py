from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.product import ProductCreate, ProductOut
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
