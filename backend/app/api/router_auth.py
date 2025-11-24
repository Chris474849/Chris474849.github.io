from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.auth import Login, TokenOut
from app.services.auth_service import login_user, refresh_token

router = APIRouter()

@router.post("/login", response_model=TokenOut)
def login(data: Login, db: Session = Depends(get_db)):
    tokens = login_user(data.email, data.password, db)
    return tokens

@router.post("/refresh", response_model=TokenOut)
def refresh(rt: str, db: Session = Depends(get_db)):
    tokens = refresh_token(rt, db)
    return tokens
