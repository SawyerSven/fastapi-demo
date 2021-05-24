from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from schemas.main import ProductionCreate
from schemas.main import Production
from database.main import SessionLocal
from controller.production import create_product

router = APIRouter(prefix='/product', tags=['product'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/production/', response_model=Production)
def create_production(production: ProductionCreate, db: Session = Depends(get_db)):
    return create_product(db=db, production=production)
