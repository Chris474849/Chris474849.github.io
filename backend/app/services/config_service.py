import json
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.config import Config


def get_default_config(db: Session):
    row = db.query(Config).filter(Config.status == "default").first()
    if not row:
        raise HTTPException(404, "No default config")
    return json.loads(row.data)


def get_current_config(db: Session):
    row = db.query(Config).filter(Config.status == "current").first()
    if not row:
        raise HTTPException(404, "No current config")
    return json.loads(row.data)
