from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class QualityBase(BaseModel):
    team: str
    date: datetime = datetime.today()
    demand_count: int
    once_pass_count: int
    dev_review_count: int
    dev_review_pass_count: int
    use_case_count: int
    use_case_pass_count: int
    publish_count: Optional[int]
    publish_not_modify_count: Optional[int]


class QualityCreate(QualityBase):
    pass


class Quality(QualityBase):
    id: int
    product_id: int

    class Config:
        orm_mode = True


class ProductionBase(BaseModel):
    name: str = Field(..., max_length=20)
    type: int = Field(..., description="1:官网项目,2:非官网项目")


class ProductionCreate(ProductionBase):
    pass


class Production(ProductionBase):
    id: int
    qualities: List[QualityBase] = []

    class Config:
        orm_mode = True
