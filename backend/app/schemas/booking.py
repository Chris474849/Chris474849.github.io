from pydantic import BaseModel, EmailStr
from typing import Optional

# Datos base (comunes)
class BookingBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    service: str
    date: str
    message: Optional[str] = None

# Para crear (todo lo del base es necesario)
class BookingCreate(BookingBase):
    pass

# Para actualizar (todo es opcional)
class BookingUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    service: Optional[str] = None
    date: Optional[str] = None
    message: Optional[str] = None

# Para devolver al cliente (incluye el ID)
class BookingOut(BookingBase):
    id: int

    class Config:
        orm_mode = True