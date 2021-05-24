from sqlalchemy.orm import Session
from datetime import datetime
from sqa.models import qualities
from sqa.schemas import main as schema_qualities


# 创建一条质量报告
def create_quality(db: Session, quality: schema_qualities.QualityCreate):
    quality.date = datetime.date(quality.date)
    db_quality = qualities.Quality(**quality.dict())
    db.add(db_quality)
    db.commit()
    db.refresh(db_quality)
    return db_quality
