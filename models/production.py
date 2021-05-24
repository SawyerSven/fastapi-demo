from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship
from database.main import Base


class Production(Base):
    __tablename__ = "productions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(Integer, index=True)

    qualities = relationship('Quality', back_populates="productions")
