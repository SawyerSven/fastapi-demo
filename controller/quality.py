from datetime import datetime

from sqlalchemy.orm import Session
from models.qualities import Quality
from schemas.main import QualityCreate


def get_qualities_controller(db: Session, offset: int, limit: int):
    return db.query(Quality).offset(offset).limit(limit).all()


def create_quality_controller(db: Session, quality: QualityCreate, production_id: int):
    db_quality = Quality(**quality.dict(), production_id=production_id)
    db.add(db_quality)
    db.commit()
    db.refresh(db_quality)
    return db_quality
