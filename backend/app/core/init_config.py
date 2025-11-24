import json
from sqlalchemy.orm import Session
from app.models.config import Config

DEFAULT_CONFIG = {
    "siteName": "DY Prods",
    "tagline": "Capturando momentos, creando recuerdos",
    "hero": {
        "title": "DY Prods",
        "subtitle": "Capturando momentos, creando recuerdos",
        "ctaText": "Reserva ahora",
        "backgroundImage": "https://via.placeholder.com/1920x1080/2c3e50/ffffff?text=DY+Prods"
    },
    "services": {
        "title": "Nuestros Servicios",
        "items": [
            {
                "id": 1,
                "icon": "fas fa-camera",
                "title": "Sesiones Fotográficas",
                "description": "Capturamos tu esencia con retratos profesionales para individuos, parejas y familias.",
                "fullDescription": "Nuestras sesiones fotográficas están diseñadas...",
                "detailImage": "/retrato.jpg",
                "duration": "1-3 horas",
                "price": "$150 USD",
                "idealFor": "Individuos, parejas, familias",
                "includes": [
                    "Sesión fotográfica completa",
                    "Edición profesional de imágenes",
                    "20-30 fotos en alta resolución",
                    "Galería online privada",
                    "Consulta previa de styling"
                ]
            },
            {
                "id": 2,
                "icon": "fas fa-film",
                "title": "Videografía",
                "description": "Inmortalizamos tus eventos importantes...",
                "fullDescription": "Creamos videos cinematográficos...",
                "detailImage": "https://via.placeholder.com/600x400/2c3e50/ffffff?text=Videografia",
                "duration": "2-8 horas",
                "price": "$300 USD",
                "idealFor": "Eventos, bodas, corporativos",
                "includes": [
                    "Grabación en 4K",
                    "Audio profesional",
                    "Edición cinematográfica",
                    "Video final de 3-10 minutos",
                    "Material en bruto incluido",
                    "Música libre de derechos"
                ]
            },
            {
                "id": 3,
                "icon": "fas fa-building",
                "title": "Fotografía Comercial",
                "description": "Elevamos tu marca con fotografía profesional...",
                "fullDescription": "Especializados en fotografía comercial...",
                "detailImage": "https://via.placeholder.com/600x400/e67e22/ffffff?text=Comercial",
                "duration": "2-4 horas",
                "price": "$250 USD",
                "idealFor": "Empresas, productos, marcas",
                "includes": [
                    "Fotografía de productos",
                    "Retratos corporativos",
                    "Fotografía de espacios",
                    "Edición profesional",
                    "Formatos optimizados para web",
                    "Derechos comerciales incluidos"
                ]
            }
        ]
    },
    "portfolio": {
        "title": "Nuestro Portafolio",
        "images": [
            {"id": 1, "url": "/retrato.jpg", "alt": "Fotografía de retrato"},
            {"id": 2, "url": "/evento.jpg", "alt": "Fotografía de evento"},
            {"id": 3, "url": "/comercial.jpg", "alt": "Fotografía comercial"},
            {"id": 4, "url": "/producto.jpg", "alt": "Fotografía de producto"},
            {"id": 5, "url": "/boda.jpg", "alt": "Fotografía de boda"},
            {"id": 6, "url": "/artistica.jpeg", "alt": "Fotografía artística"}
        ]
    },
    "about": {
        "title": "Sobre DY Prods",
        "image": "/equipo.jpeg",
        "subtitle": "Somos un equipo apasionado...",
        "description": [
            "Fundado en 2015, DY Prods se ha convertido...",
            "Trabajamos con equipos de última generación..."
        ]
    },
    "contact": {
        "title": "Reserva tu Sesión",
        "services": [
            {"value": "retrato", "label": "Fotografía de Retrato"},
            {"value": "evento", "label": "Fotografía de Evento"},
            {"value": "comercial", "label": "Fotografía Comercial"},
            {"value": "video", "label": "Videografía"}
        ],
        "staff": [
            {
                "id": 1,
                "value": "daineris",
                "name": "Daineris",
                "specialty": "Fotografía de Retratos y Eventos",
                "image": "https://via.placeholder.com/150x150/e67e22/ffffff?text=D"
            },
            {
                "id": 2,
                "value": "yoi",
                "name": "Yoi",
                "specialty": "Videografía y Fotografía Comercial",
                "image": "https://via.placeholder.com/150x150/2c3e50/ffffff?text=Y"
            }
        ]
    },
    "requests": [],
    "footer": {
        "description": "Tu estudio fotográfico...",
        "contact": {
            "phones": ["+53 56601651", "+53 55494545"],
            "email": "dyprods0581@gmail.com"
        },
        "schedule": {
            "weekdays": "Lunes a Viernes: 9:00 AM - 6:00 PM",
            "saturday": "Sábados: 10:00 AM - 3:00 PM",
            "sunday": "Domingos: Cerrado"
        },
        "social": {
            "facebook": "#",
            "instagram": "https://www.instagram.com/DY_Prods/",
            "twitter": "#",
            "linkedin": "#"
        }
    },
    "theme": {
        "primaryColor": "#007bff",
        "secondaryColor": "#e67e22",
        "backgroundColor": "#ffffff",
        "textColor": "#333333"
    }
}

def init_config(db: Session):
    exists = db.query(Config).count()
    if exists == 0:
        default_json = json.dumps(DEFAULT_CONFIG)
        db.add(Config(status="default", data=default_json))
        db.add(Config(status="current", data=default_json))
        db.commit()
