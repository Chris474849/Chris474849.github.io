import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.config import Config

router = APIRouter()

@router.get("/config")
def list_all(db: Session = Depends(get_db)):
    rows = db.query(Config).all()
    return [{"id": r.id, "status": r.status, "data": json.loads(r.data)} for r in rows]

@router.get("/config/default")
def get_default(db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.status == "default").first()
    if not row:
        raise HTTPException(404, "No default config")
    return json.loads(row.data)

@router.get("/config/current")
def get_current(db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.status == "current").first()
    if not row:
        raise HTTPException(404, "No current config")
    return json.loads(row.data)

@router.post("/config/default")
def set_default(data: dict, db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.status == "default").first()
    
    if not row:
        raise HTTPException(404, "No default config record found to update.")
    
    row.data = json.dumps(data)
    db.commit()
    return {"ok": True, "message": "Default configuration updated successfully."}

@router.post("/config/current")
def set_current(data: dict, db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.status == "current").first()
    
    if not row:
        raise HTTPException(404, "No current config record found to update.")
    
    row.data = json.dumps(data)
    db.commit()
    return {"ok": True, "message": "Current configuration updated successfully."}

@router.get("/config/{config_id}")
def get_config(config_id: int, db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.id == config_id).first()
    if not row:
        raise HTTPException(404, "Config not found")
    return {"id": row.id, "status": row.status, "data": json.loads(row.data)}

@router.put("/config/{config_id}")
def update_config(config_id: int, data: dict, db: Session = Depends(get_db)):
    row = db.query(Config).filter(Config.id == config_id).first()
    if not row:
        raise HTTPException(404, "Config not found")
    row.data = json.dumps(data)
    db.commit()
    return {"ok": True}