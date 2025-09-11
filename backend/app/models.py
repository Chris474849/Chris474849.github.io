from typing import Optional
from sqlmodel import SQLModel, Field

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    phone: Optional[str] = None
    service: Optional[str] = None
    date: Optional[str] = None       # ISO date string (YYYY-MM-DD)
    message: Optional[str] = None
