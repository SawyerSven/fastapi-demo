# from fastapi import Depends, APIRouter
# from sqlalchemy.orm import Session
# from ..database.main import SessionLocal
#
# from sqa.schemas import main
# from sqa.controller import quality as quality_controller
#
# router = APIRouter(prefix='/qualities', tags=['official'])
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# @router.post('/')
# def create_quality(quality: main.QualityCreate, db: Session = Depends(get_db)):
#     return quality_controller.create_quality(db=db, quality=quality)
