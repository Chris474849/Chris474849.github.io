from fastapi import FastAPI
from app.api.router_user import router as user_router
from app.api.router_auth import router as auth_router
from app.api.router_role import router as role_router
from app.core.database import Base, engine
from app.core.database import SessionLocal
from app.services.user_service import create_default_roles
from app.middlewares.global_middleware import global_middleware
from app.api.router_booking import router as booking_router
from app.core.auto_migrator import init_auto_migrator
from app.core.init_config import init_config
from app.api.router_request import router as request_router
from app.api.router_config import router as config_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

init_auto_migrator(app)


@app.on_event("startup")
def init_roles():
    db = SessionLocal()
    create_default_roles(db)
    init_config(db)
    db.close()

app.middleware("http")(global_middleware)

app.include_router(user_router, tags=["User"])
app.include_router(auth_router, tags=["Auth"])
app.include_router(role_router, tags=["Role"])
app.include_router(booking_router, tags=["Bookings"])
app.include_router(request_router, tags=["Request"])
app.include_router(config_router, tags=["Config"])
