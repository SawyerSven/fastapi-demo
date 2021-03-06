from sqlalchemy.orm import Session
from schemas import main as schemas
from models.production import Production


def create_product(db: Session, production: schemas.ProductionCreate):
    db_production = Production(**production.dict())
    db.add(db_production)
    db.commit()
    db.refresh(db_production)
    return db_production


def get_all_production(offset: int, limit: int, db: Session):
    return db.query(Production).offset(offset).limit(limit).all()
