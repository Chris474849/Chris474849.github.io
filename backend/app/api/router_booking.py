from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.deps import get_db
from app.schemas.booking import BookingCreate, BookingOut, BookingUpdate
from app.services import booking_service

router = APIRouter()

@router.get("/bookings", response_model=List[BookingOut])
def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = booking_service.get_bookings(db, skip=skip, limit=limit)
    return bookings

@router.post("/bookings", response_model=BookingOut)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    return booking_service.create_booking(db=db, booking=booking)

@router.get("/bookings/{booking_id}", response_model=BookingOut)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking_service.get_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.put("/bookings/{booking_id}", response_model=BookingOut)
def update_booking(booking_id: int, booking: BookingUpdate, db: Session = Depends(get_db)):
    db_booking = booking_service.update_booking(db, booking_id, booking)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

@router.delete("/bookings/{booking_id}")
def delete_booking(booking_id: int, db: Session = Depends(get_db)):
    success = booking_service.delete_booking(db, booking_id)
    if not success:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"ok": True}