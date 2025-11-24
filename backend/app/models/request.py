from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    email = Column(String, index=True)
    nombre = Column(String)
    telefono = Column(String)
    servicio = Column(String)
    fecha = Column(Date)
    personal = Column(String)
    mensaje = Column(String)

    user = relationship("User")
