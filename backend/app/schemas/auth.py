from pydantic import BaseModel, EmailStr

class Login(BaseModel):
    email: EmailStr
    password: str

class TokenOut(BaseModel):
    access: str
    refresh: str
    role: str

class RegisterIn(BaseModel):
    email: EmailStr
    role: str
    password: str | None = None

class VerifyIn(BaseModel):
    email: EmailStr
    code: str

class RegisterOut(BaseModel):
    id: int
    email: EmailStr
    role: str
    is_verified: bool

    class Config:
        from_attributes = True
