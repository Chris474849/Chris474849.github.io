from pydantic import BaseModel
from datetime import date

class RequestBase(BaseModel):
    email: str
    nombre: str
    telefono: str
    servicio: str
    fecha: date
    personal: str
    mensaje: str

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    email: str | None = None
    nombre: str | None = None
    telefono: str | None = None
    servicio: str | None = None
    fecha: date | None = None
    personal: str | None = None
    mensaje: str | None = None

class RequestOut(RequestBase):
    id: int
    class Config:
        orm_mode = True

class RequestValidateIn(BaseModel):
    email: str
    servicio: str
    fecha: date

class RequestValidateOut(BaseModel):
    allowed: bool
    reason: str | None = None
