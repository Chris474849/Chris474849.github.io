from sqlalchemy.orm import Session
from app.models.user import User
from app.models.password import Password
from app.models.token import RefreshToken
from app.core.security import verify_password, create_access_token, create_refresh_token, decode_token

def login_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    if user.role.name == "client":
        return None
    if not user.password:
        return None
    if not verify_password(password, user.password.hash):
        return None
    access = create_access_token({"sub": str(user.id)})
    refresh = create_refresh_token({"sub": str(user.id)})
    role = user.role.name
    print(role)
    rt = RefreshToken(token=refresh, user_id=user.id)
    db.add(rt)
    db.commit()
    return {"access": access, "refresh": refresh, "role": role}

def refresh_token(token: str, db: Session):
    data = decode_token(token)
    user_id = int(data["sub"])
    stored = db.query(RefreshToken).filter(RefreshToken.token == token, RefreshToken.revoked == False).first()
    if not stored:
        return None
    stored.revoked = True
    db.commit()
    access = create_access_token({"sub": str(user_id)})
    refresh = create_refresh_token({"sub": str(user_id)})
    rt = RefreshToken(token=refresh, user_id=user_id)
    db.add(rt)
    db.commit()
    return {"access": access, "refresh": refresh}
