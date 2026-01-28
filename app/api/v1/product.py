from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.deps import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse  # DTO 임포트
from app.crud import product_crud # CRUD 로직 임포트

router = APIRouter(prefix="/products", tags=["Product"])

# 1. Create: 상품 등록 (Validation 포함)
@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    if product.price <= 0:
        raise HTTPException(status_code=400, detail="가격은 0보다 커야 합니다.")
    return product_crud.create_product(db, product)

# 2. Read: 활성화된 상품만 조회 (is_active=True)
@router.get("/", response_model=List[ProductResponse])
def get_active_products(db: Session = Depends(get_db)):
    # CRUD 레이어에서 필터링 로직을 수행하도록 호출
    return product_crud.get_active_products(db)

# 3. Update: 재고(stock) 수정
@router.patch("/{product_id}/stock", response_model=ProductResponse)
def update_product_stock(product_id: int, stock: int, db: Session = Depends(get_db)):
    updated_product = product_crud.update_stock(db, product_id, stock)
    if not updated_product:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
    return updated_product

# 4. Delete: Soft Delete (is_active = False)
@router.delete("/{product_id}", response_model=ProductResponse)
def soft_delete_product(product_id: int, db: Session = Depends(get_db)):
    deleted_product = product_crud.soft_delete(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="상품을 찾을 수 없습니다.")
    return deleted_product