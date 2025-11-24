from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.schemas.auth import RegisterIn, RegisterOut, VerifyIn
from app.api.deps import get_db
from app.services import user_service
from app.services.user_service import create_user_with_verification, verify_user_code
from app.core.mailer import send_verification_email, send_mail
from app.services.user_service import create_user_with_verification, verify_user_code, resend_code

router = APIRouter()

@router.post("/users", response_model=UserOut)
def create_user_route(data: UserCreate, db: Session = Depends(get_db)):
    result = user_service.create_user(data, db)
    
    # Manejo de errores
    if result == "exists":
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if result == "role_error":
        raise HTTPException(status_code=400, detail="Role does not exist")

    # NUEVO: Verificamos si el resultado es un diccionario con error de email
    if isinstance(result, dict) and result.get("error") == "invalid_email":
        # Aquí enviamos el mensaje exacto que nos dio la librería (ej: dominio no existe)
        raise HTTPException(status_code=400, detail=result["msg"])

    if result is None:
        raise HTTPException(status_code=400, detail="Unknown error creating user")
        
    return UserOut(id=result.id, email=result.email, role=result.role.name)

# --- READ LIST ---
@router.get("/users", response_model=List[UserOut])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_service.get_all_users(db, skip, limit)
    # Mapeo manual o usar ORM mode de Pydantic
    return [UserOut(id=u.id, email=u.email, role=u.role.name) for u in users]

# --- READ ONE ---
@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(id=user.id, email=user.email, role=user.role.name)

@router.put("/users/{user_id}", response_model=UserOut)
def update_user_route(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    result = user_service.update_user(user_id, data, db)
    
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # NUEVO: Manejo del mensaje dinámico
    if isinstance(result, dict) and result.get("error") == "invalid_email":
        raise HTTPException(status_code=400, detail=result["msg"])
        
    if result == "email_exists":
        raise HTTPException(status_code=400, detail="New email is already in use")
        
    if result == "role_error":
        raise HTTPException(status_code=400, detail="Role does not exist")
        
    return UserOut(id=result.id, email=result.email, role=result.role.name)

# --- DELETE ---
@router.delete("/users/{user_id}")
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    success = user_service.delete_user(user_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

@router.post("/register", response_model=RegisterOut)
def register(data: RegisterIn, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user, status = create_user_with_verification(db, data.email, data.role, data.password)
    if user is None:
        if status == "invalid_email":
            raise HTTPException(400, "Email inválido")
        if status == "password_required":
            raise HTTPException(400, "Password requerida")
        if status == "role_not_found":
            raise HTTPException(400, "Rol no existe")
        raise HTTPException(400, "Error")
    if status == "exists":
        return RegisterOut(id=user.id, email=user.email, role=user.role.name, is_verified=user.is_verified)
    code = status
    background_tasks.add_task(send_verification_email, user.email, code)
    return RegisterOut(id=user.id, email=user.email, role=user.role.name, is_verified=user.is_verified)

@router.post("/verify")
def verify(data: VerifyIn, db: Session = Depends(get_db)):
    ok, status = verify_user_code(db, data.email, data.code)
    if not ok:
        if status == "blocked":
            raise HTTPException(400, "Cuenta bloqueada por demasiados intentos")
        if status == "expired":
            raise HTTPException(400, "Código expirado")
        raise HTTPException(400, "Código inválido")
    return {"ok": True}

@router.post("/resend")
def resend(email: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user, status = resend_code(db, email)
    if user is None:
        if status == "blocked":
            raise HTTPException(400, "Cuenta bloqueada")
        raise HTTPException(404, "Usuario no encontrado")
    background_tasks.add_task(send_verification_email, user.email, user.verification_code)
    return {"ok": True}

@router.get("/user-id")
def get_user_id(email: str, db: Session = Depends(get_db)):
    user_id = user_service.get_user_id_by_email(db, email)
    if user_id is None:
        raise HTTPException(404, "Usuario no encontrado")
    return {"id": user_id}
