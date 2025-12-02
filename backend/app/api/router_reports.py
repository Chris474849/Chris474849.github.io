from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.services.user_service import get_all_users
from app.reports.user_report import build_users_pdf
from app.reports.role_report import build_roles_pdf
from app.reports.request_report import build_requests_pdf
from app.reports.config_report import build_config_pdf
from app.services.config_service import get_current_config, get_default_config
from app.models.role import Role
from app.services.request_service import list_requests  

router = APIRouter()

@router.get("/reports/users")
def report_users(db: Session = Depends(get_db)):
    config = get_current_config(db)
    users = get_all_users(db)

    pdf_buffer = build_users_pdf(users, config)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=usuarios.pdf"}
    )

@router.get("/reports/roles")
def report_roles(db: Session = Depends(get_db)):
    config = get_current_config(db)
    roles = db.query(Role).all()

    pdf = build_roles_pdf(roles, config)
    return StreamingResponse(pdf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=roles.pdf"
    })

@router.get("/reports/requests")
def report_requests(db: Session = Depends(get_db)):
    config = get_current_config(db)
    requests = list_requests(db)

    pdf = build_requests_pdf(requests, config)
    return StreamingResponse(pdf, media_type="application/pdf", headers={
        "Content-Disposition": "attachment; filename=requests.pdf"
    })

@router.get("/reports/config/default")
def report_config_default(db: Session = Depends(get_db)):
    config_header = get_current_config(db)
    config_json = get_default_config(db)

    pdf = build_config_pdf(config_json, config_header)
    return StreamingResponse(pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=config_default.pdf"}
    )

@router.get("/reports/config/current")
def report_config_current(db: Session = Depends(get_db)):
    config_json = get_current_config(db)

    pdf = build_config_pdf(config_json, config_json)
    return StreamingResponse(pdf,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=config_current.pdf"}
    )
