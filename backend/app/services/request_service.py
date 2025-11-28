from sqlalchemy.orm import Session
from datetime import date
from app.models.request import Request
from app.schemas.request import (
    RequestCreate, RequestUpdate, RequestValidateIn, RequestValidateOut
)
from app.models.config import Config
import json

def create_request(db: Session, data: RequestCreate):
    obj = Request(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_request(db: Session, request_id: int):
    return db.query(Request).filter(Request.id == request_id).first()

def list_requests(db: Session):
    return db.query(Request).all()

def update_request(db: Session, request_id: int, data: RequestUpdate):
    obj = db.query(Request).filter(Request.id == request_id).first()
    if not obj:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_request(db: Session, request_id: int):
    obj = db.query(Request).filter(Request.id ==request_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True

def extract_service_hours(service_item):
    duration = service_item["duration"]
    last_num = duration.strip().split("-")[-1].replace("horas", "").replace("hora", "").strip()
    return int(last_num)

def validate_request_logic(db: Session, data: RequestValidateIn):
    same_email_same_day = db.query(Request).filter(
        Request.email == data.email,
        Request.fecha == data.fecha
    ).first()

    if same_email_same_day:
        return RequestValidateOut(
            allowed=False,
            reason="Este usuario ya tiene una solicitud en esa fecha"
        )

    config = db.query(Config).order_by(Config.id.desc()).first()
    if not config:
        return RequestValidateOut(allowed=False, reason="No existe configuración del sistema")

    config_json = json.loads(config.data)
    items = config_json["services"]["items"]

    service_item = next((i for i in items if i["title"] == data.servicio), None)
    if not service_item:
        return RequestValidateOut(
            allowed=False,
            reason="El servicio no está configurado"
        )

    requested_hours = extract_service_hours(service_item)

    requests_same_day = db.query(Request).filter(Request.fecha == data.fecha).all()

    total_hours = 0
    for r in requests_same_day:
        srv = next((i for i in items if i["title"] == r.servicio), None)
        if srv:
            total_hours += extract_service_hours(srv)

    if total_hours > 8:
        return RequestValidateOut(
            allowed=False,
            reason="La carga de trabajo del día ya excede las 8 horas"
        )

    if total_hours + requested_hours > 8:
        return RequestValidateOut(
            allowed=False,
            reason="No hay disponibilidad suficiente para este servicio"
        )

    return RequestValidateOut(
        allowed=True,
        reason="Disponible"
    )
