from pydantic import BaseModel, EmailStr
from typing import Optional

# --- CREATE (Ya lo tenías, lo mantenemos igual) ---
class UserCreate(BaseModel):
    email: EmailStr
    role: str
    password: str | None = None

# --- UPDATE (Nuevo: para editar usuario) ---
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    password: Optional[str] = None

# --- OUT (Ya lo tenías, lo usamos para leer) ---
class UserOut(BaseModel):
    id: int
    email: EmailStr
    is_verified: bool
    role: str  # Devolvemos el nombre del rol, no el ID

    class Config:
        orm_mode = True