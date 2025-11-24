from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")
    password = relationship("Password", uselist=False, back_populates="user")
    is_verified = Column(Boolean, default=False)
    verification_code = Column(String, nullable=True, index=True)
    verification_expires_at = Column(DateTime, nullable=True)
    verification_attempts = Column(Integer, default=0)
    is_blocked = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
