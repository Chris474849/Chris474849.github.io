from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.role import Role
# Agrega esto a tus imports
from fastapi import HTTPException 
from pydantic import BaseModel

router = APIRouter()

@router.get("/roles")
def list_roles(db: Session = Depends(get_db)):
    return db.query(Role).all()

@router.post("/roles")
def create_role(name: str, db: Session = Depends(get_db)):
    r = Role(name=name)
    db.add(r)
    db.commit()
    db.refresh(r)
    return r

@router.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    r = db.query(Role).filter(Role.id == role_id).first()
    if not r:
        return None
    db.delete(r)
    db.commit()
    return {"ok": True}


class RoleUpdate(BaseModel):
    name: str

@router.put("/roles/{role_id}")
def update_role(role_id: int, data: RoleUpdate, db: Session = Depends(get_db)):
    role = db.query(Role).filter(Role.id == role_id).first()
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    # Verificar duplicado de nombre si cambia
    if data.name != role.name:
        exists = db.query(Role).filter(Role.name == data.name).first()
        if exists:
             raise HTTPException(status_code=400, detail="Role name already exists")
        role.name = data.name
    
    db.commit()
    db.refresh(role)
    return role