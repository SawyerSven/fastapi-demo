from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.main import ProductionCreate
from schemas.main import Production
from database.main import SessionLocal
from controller.production import create_product, get_all_production as get_all_production_controller

router = APIRouter(prefix='/product', tags=['产品线'])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 查询所有产品线
@router.get('/', response_model=List[Production])
def get_all_production(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_all_production_controller(offset=offset, limit=limit, db=db)


# 新建产品线
@router.post('/', response_model=Production, description="新建产品线", summary='新建产品线', name='12321')
def create_production(production: ProductionCreate, db: Session = Depends(get_db)):
    return create_product(db=db, production=production)
