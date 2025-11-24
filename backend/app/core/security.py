from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt

# CAMBIO VITAL: Reemplazamos "bcrypt" por "pbkdf2_sha256"
# Esto evita la dependencia de librerías C que causan el AttributeError.
pwd = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

SECRET_KEY = "SECRET_KEY_CHANGE"
ALGO = "HS256"

def hash_password(password: str) -> str:
    return pwd.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd.verify(password, hashed)

def create_access_token(data: dict, expires=15):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)

def create_refresh_token(data: dict, expires=60*24*7):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)

def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGO])