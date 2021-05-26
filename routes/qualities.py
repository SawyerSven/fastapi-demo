from typing import List
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database.main import SessionLocal
from controller.quality import get_qualities_controller, create_quality_controller
from schemas.main import Quality, QualityCreate

router = APIRouter(prefix='/qualities', tags=['质量报告'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/', name='获取所有的质量报告', response_model=List[Quality])
def get_qualities(db: Session = Depends(get_db), offset: int = 0, limit: int = 100):
    return get_qualities_controller(offset=offset, limit=limit, db=db)


@router.post('/{production_id}/', name="新建质量报告", response_model=Quality)
def create_quality(quality: QualityCreate, production_id: int, db: Session = Depends(get_db)):
    return create_quality_controller(db=db, quality=quality, production_id=production_id)
