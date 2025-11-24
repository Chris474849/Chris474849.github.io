from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Config(Base):
    __tablename__ = "config"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True, nullable=True)
    data = Column(Text, nullable=True)
