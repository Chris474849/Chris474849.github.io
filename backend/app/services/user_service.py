from sqlalchemy.orm import Session
# Asegúrate de importar EmailNotValidError
from email_validator import validate_email, EmailNotValidError 
from app.core.security import hash_password
from app.models.user import User
from app.models.role import Role
from app.models.password import Password
from datetime import datetime, timedelta
import random

def create_default_roles(db: Session):
    roles = ["admin", "worker", "client"]
    for r in roles:
        exists = db.query(Role).filter(Role.name == r).first()
        if not exists:
            db.add(Role(name=r))
    db.commit()
    

def generate_code():
    return f"{random.randint(0, 999999):06d}"

def create_user_with_verification(db: Session, email: str, role_name: str, password: str | None):
    try:
        valid = validate_email(email)
        email_norm = valid.normalized
    except EmailNotValidError:
        return None, "invalid_email"

    existing = db.query(User).filter(User.email == email_norm).first()
    if existing:
        return existing, "exists"

    role = db.query(Role).filter(Role.name == role_name).first()
    if not role:
        return None, "role_not_found"

    user = User(email=email_norm, role_id=role.id)
    db.add(user)
    db.commit()
    db.refresh(user)

    if role_name in ["admin", "worker"]:
        if not password:
            return None, "password_required"
        pwd = Password(hash=hash_password(password), user_id=user.id)
        db.add(pwd)
        db.commit()

    code = generate_code()
    expires = datetime.utcnow() + timedelta(minutes=15)

    user.verification_code = code
    user.verification_expires_at = expires
    user.verification_attempts = 0
    user.is_blocked = False
    user.is_verified = False

    db.add(user)
    db.commit()
    return user, code

def verify_user_code(db: Session, email: str, code: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return False, "not_found"
    if user.is_blocked:
        return False, "blocked"
    if user.is_verified:
        return True, "already_verified"
    if not user.verification_code:
        return False, "no_code"
    if datetime.utcnow() > user.verification_expires_at:
        return False, "expired"
    if code.strip() != user.verification_code.strip():
        user.verification_attempts += 1
        if user.verification_attempts >= 5:
            user.is_blocked = True
        db.commit()
        return False, "invalid"
    user.is_verified = True
    user.verification_code = None
    user.verification_expires_at = None
    user.verification_attempts = 0
    db.commit()
    return True, "verified"

def resend_code(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None, "not_found"
    if user.is_blocked:
        return None, "blocked"
    code = generate_code()
    expires = datetime.utcnow() + timedelta(minutes=15)
    user.verification_code = code
    user.verification_expires_at = expires
    user.verification_attempts = 0
    db.commit()
    return user, code

# --- CRUD CREATE ---
def create_user(data, db: Session):
    # 1. Validar email, verificar existencia, verificar rol (Lógica anterior OK)
    print(data.email)
    try:
        valid = validate_email(data.email, check_deliverability=True)
        email_normalized = valid.normalized
    except EmailNotValidError as e:
        return {"error": "invalid_email", "msg": str(e)}
    
    exists = db.query(User).filter(User.email == email_normalized).first()
    if exists:
        return "exists" 

    role = db.query(Role).filter(Role.name == data.role).first()
    if not role:
        return "role_error"

    # 4. Crear Usuario: Añadir a la sesión
    user = User(email=email_normalized, role_id=role.id)
    db.add(user)
    
    # VITAL: Usamos flush() para obtener el user.id sin hacer COMMIT final
    try:
        db.flush() 
        db.refresh(user) 
    except Exception as e:
        # Si el flush falla por alguna razón (ej. restricción), hacemos rollback
        db.rollback()
        raise e

    # 5. Crear Password
    if data.password:
        try:
            # Prevención: Truncamos la contraseña para evitar el ValueError de 72 bytes
            pwd_hash = hash_password(data.password)

            pwd = Password(hash=pwd_hash, user_id=user.id)
            db.add(pwd)
            
        except Exception:
            # SI EL HASHING FALLA (AttributeError, ValueError, etc.), 
            # revertimos la creación del usuario y re-lanzamos el error.
            db.rollback() 
            raise 

    # 6. COMMIT ÚNICO y ATÓMICO: Si llegamos aquí, el usuario y el password se guardan juntos.
    db.commit() 
    
    return user

# --- CRUD READ ---
def get_user_by_id(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()

# --- CRUD UPDATE ---
def update_user(user_id: int, data, db: Session):
    user = get_user_by_id(user_id, db)
    if not user:
        return None

    # Si se actualiza el email
    if data.email and data.email != user.email:
        try:
            valid = validate_email(data.email, check_deliverability=True)
            email_normalized = valid.normalized
        except EmailNotValidError as e:
            return {"error": "invalid_email", "msg": str(e)}

        exists = db.query(User).filter(User.email == email_normalized).first()
        if exists:
            return "email_exists"
        
        user.email = email_normalized

    # Si se actualiza el rol
    if data.role:
        role = db.query(Role).filter(Role.name == data.role).first()
        if not role:
            return "role_error"
        user.role_id = role.id

    # Si se actualiza la contraseña
    if data.password:
        new_hash = hash_password(data.password)
        if user.password:
            user.password.hash = new_hash 
        else:
            pwd = Password(hash=new_hash, user_id=user.id)
            db.add(pwd)
    
    db.commit()
    db.refresh(user)
    return user

# --- CRUD DELETE ---
def delete_user(user_id: int, db: Session):
    user = get_user_by_id(user_id, db)
    if not user:
        return False
    
    if user.password:
        db.delete(user.password)
        
    db.delete(user)
    db.commit()
    return True

def get_user_id_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None
    return user.id
