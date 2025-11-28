from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.request import RequestCreate, RequestUpdate, RequestOut
from app.services.request_service import (
    create_request,
    get_request,
    list_requests,
    update_request,
    delete_request
)
from app.schemas.request import (
    RequestCreate, RequestUpdate, RequestOut, RequestValidateIn, RequestValidateOut
)

from app.services.request_service import (
    create_request, get_request, list_requests, update_request,
    delete_request, validate_request_logic
)

router = APIRouter(prefix="/requests")

@router.post("/", response_model=RequestOut)
def create_req(data: RequestCreate, db: Session = Depends(get_db)):
    return create_request(db, data)

@router.get("/", response_model=list[RequestOut])
def list_req(db: Session = Depends(get_db)):
    return list_requests(db)

@router.get("/{request_id}", response_model=RequestOut)
def get_req(request_id: int, db: Session = Depends(get_db)):
    obj = get_request(db, request_id)
    if not obj:
        raise HTTPException(404, "Request not found")
    return obj

@router.put("/{request_id}", response_model=RequestOut)
def update_req(request_id: int, data: RequestUpdate, db: Session = Depends(get_db)):
    obj = update_request(db, request_id, data)
    if not obj:
        raise HTTPException(404, "Request not found")
    return obj

@router.delete("/{request_id}")
def delete_req(request_id: int, db: Session = Depends(get_db)):
    ok = delete_request(db, request_id)
    if not ok:
        raise HTTPException(404, "Request not found")
    return {"ok": True}

@router.post("/validate", response_model=RequestValidateOut)
def validate_req(data: RequestValidateIn, db: Session = Depends(get_db)):
    result = validate_request_logic(db, data)
    if not result.allowed:
        raise HTTPException(400, result.reason)
    return result