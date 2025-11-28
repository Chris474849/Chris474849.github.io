from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    role: str
    password: str | None = None

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    password: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_verified: bool
    role: str

    class Config:
        orm_mode = True