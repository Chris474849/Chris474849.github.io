from sqlalchemy.orm import Session
from app.models.request import Request
from app.schemas.request import RequestCreate, RequestUpdate

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
    obj = db.query(Request).filter(Request.id == request_id).first()
    if not obj:
        return False
    db.delete(obj)
    db.commit()
    return True
