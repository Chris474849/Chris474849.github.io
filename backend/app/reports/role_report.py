# app/reports/role_report.py
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from app.reports.helpers import draw_header

def build_roles_pdf(roles, config):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    start_y = draw_header(pdf, config)
    y = start_y

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, 690, "Listado de Roles")

    data = [["ID", "Nombre"]]
    for r in roles:
        data.append([str(r.id), r.name])

    table = Table(data, colWidths=[80, 400])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkgray),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.gray),
        ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
    ]))

    table.wrapOn(pdf, 40, 600)
    table.drawOn(pdf, 40, 600 - 20 * len(data))

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
