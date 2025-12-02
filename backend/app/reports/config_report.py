# app/reports/config_report.py
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from app.reports.helpers import draw_header

styles = getSampleStyleSheet()
normal = styles["Normal"]
title = styles["Heading2"]

def build_config_pdf(config_json, config_header):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    start_y = draw_header(pdf, config_header)
    y = start_y

    y = 690
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, y, "Configuración Completa")
    y -= 30

    def write(text, size=10, bold=False, space=12):
        nonlocal y
        font = "Helvetica-Bold" if bold else "Helvetica"
        pdf.setFont(font, size)
        pdf.drawString(40, y, text)
        y -= space
        if y < 60:
            pdf.showPage()
            start_y = draw_header(pdf, config_header)
            y = start_y


    # === CAMPOS PRINCIPALES ===
    write("Datos Generales", bold=True, size=12)
    write(f"siteName: {config_json['siteName']}")
    write(f"tagline: {config_json['tagline']}")
    y -= 10

    # === HERO ===
    write("Hero Section", bold=True, size=12)
    write(f"title: {config_json['hero']['title']}")
    write(f"subtitle: {config_json['hero']['subtitle']}")
    write(f"ctaText: {config_json['hero']['ctaText']}")
    write(f"backgroundImage: {config_json['hero']['backgroundImage']}")
    y -= 10

    # === SERVICES ===
    write("Servicios", bold=True, size=12)
    for item in config_json["services"]["items"]:
        write(f"- {item['id']}: {item['title']}", bold=True)
        write(f"  Description: {item['description']}")
        write(f"  Duration: {item['duration']}")
        write(f"  Price: {item['price']}")
        write(f"  Ideal para: {item['idealFor']}")
        write("  Includes:")
        for inc in item["includes"]:
            write(f"     * {inc}")
        y -= 10

    # === PORTFOLIO ===
    write("Portafolio", bold=True, size=12)
    for img in config_json["portfolio"]["images"]:
        write(f"- {img['id']} | {img['alt']} | {img['url']}")

    y -= 10

    # === ABOUT ===
    write("Sobre nosotros", bold=True, size=12)
    write(f"subtitle: {config_json['about']['subtitle']}")
    for p in config_json["about"]["description"]:
        write(f"- {p}")

    # === STAFF ===
    write("Staff", bold=True, size=12)
    for s in config_json["contact"]["staff"]:
        write(f"{s['name']} - {s['specialty']}")

    # === FOOTER ===
    write("Footer", bold=True, size=12)
    write(f"Email: {config_json['footer']['contact']['email']}")
    write(f"Teléfonos: {', '.join(config_json['footer']['contact']['phones'])}")

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
