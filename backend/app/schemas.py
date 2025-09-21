from pydantic import BaseModel, EmailStr
from typing import Optional

class BookingCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    service: Optional[str] = None
    date: Optional[str] = None
    message: Optional[str] = None
