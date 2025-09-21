import os
from typing import List

from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from sqlmodel import SQLModel, create_engine, Session, select

from .models import Booking
from .schemas import BookingCreate

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("base: ", BASE_DIR)
# Ajusta la ruta a tu carpeta frontend (la que contiene index.html, css/, js/)
FRONTEND_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../frontend"))

app = FastAPI(title="DY Prods - Backend")

# DEV: permitir CORS desde cualquier origen (en producción restringirlo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar la carpeta del frontend en la raíz (sirve index.html y assets tal cual)
# Esto hace que las rutas como /css/styles.css y /js/main.js funcionen sin cambios.
print("fronted: ", FRONTEND_DIR)
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

# ---- DB (SQLite local simple) ----
DB_FILE = os.path.join(BASE_DIR, "bookings.db")
sqlite_url = f"sqlite:///{DB_FILE}"
engine = create_engine(sqlite_url, echo=False, connect_args={"check_same_thread": False})

@app.on_event("startup")
def on_startup():
    # crea tablas si no existen
    SQLModel.metadata.create_all(engine)

# ---- API ----

@app.post("/api/bookings", response_model=dict)
def create_booking(booking: BookingCreate):
    # Validación ya la hace Pydantic (Email etc.)
    with Session(engine) as session:
        b = Booking.from_orm(booking)
        session.add(b)
        session.commit()
        session.refresh(b)
        return {"success": True, "booking_id": b.id}

@app.get("/api/bookings", response_model=List[dict])
def list_bookings(limit: int = 100):
    with Session(engine) as session:
        q = select(Booking).limit(limit)
        rows = session.exec(q).all()
        # convertir a dict simple
        return [r.dict() for r in rows]

@app.get("/api/health")
def health():
    return {"status": "ok"}

# Nota: Las rutas de frontend están montadas en / (StaticFiles) — los endpoints /api/* siguen funcionando.
# si prefieres servir index únicamente con FileResponse:
# @app.get("/")
# def root():
#     return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))
