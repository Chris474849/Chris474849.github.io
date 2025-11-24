from sqlalchemy.orm import Session
from app.models.booking import Booking
from app.schemas.booking import BookingCreate, BookingUpdate

def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.id == booking_id).first()

def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Booking).offset(skip).limit(limit).all()

def create_booking(db: Session, booking: BookingCreate):
    # Aquí podrías validar si la fecha ya está ocupada, etc.
    db_booking = Booking(
        name=booking.name,
        email=booking.email,
        phone=booking.phone,
        service=booking.service,
        date=booking.date,
        message=booking.message
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def update_booking(db: Session, booking_id: int, booking_in: BookingUpdate):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return None
    
    # Actualizar solo los campos que vienen en la petición
    update_data = booking_in.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_booking, key, value)

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

def delete_booking(db: Session, booking_id: int):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return False
    db.delete(db_booking)
    db.commit()
    return True