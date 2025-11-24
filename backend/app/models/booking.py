from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Booking(Base):
    __tablename__ = "booking"  # El nombre exacto de tu tabla existente

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    service = Column(String, nullable=True)
    date = Column(String, nullable=True) # Podríamos usar DateTime, pero tu tabla actual usa VARCHAR
    message = Column(String, nullable=True)