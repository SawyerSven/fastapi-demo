from sqlalchemy import String, Integer, Column, ForeignKey, Date
from sqlalchemy.orm import relationship

from database.main import Base


def normal_integer_column():
    return Column(Integer, nullable=False)


class Quality(Base):
    __tablename__ = "quality"

    id = Column(Integer, primary_key=True, index=True)
    # 项目组
    team = Column(String)
    # 日期
    date = Column(Date, nullable=False)
    # 需求数
    demand_count = normal_integer_column()
    # 需求评审一次性通过数
    once_pass_count = normal_integer_column()
    # 开发设计评审数
    dev_review_count = normal_integer_column()
    # 开发设计评审pass数
    dev_review_pass_count = normal_integer_column()
    # 用例数
    use_case_count = normal_integer_column()
    # 用例评审一次性pass数
    use_case_pass_count = normal_integer_column()
    # 发布数量
    publish_count = Column(Integer)
    # 发布无更变数
    publish_not_modify_count = Column(Integer)

    product_id = Column(Integer, ForeignKey('productions.id'))

    productions = relationship("Production", back_populates="qualities")
