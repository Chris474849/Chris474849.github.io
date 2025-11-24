from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Password(Base):
    __tablename__ = "passwords"
    id = Column(Integer, primary_key=True, index=True)
    hash = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="password")
