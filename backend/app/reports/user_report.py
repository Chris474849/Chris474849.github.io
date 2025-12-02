from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate

from app.reports.helpers import draw_header

def build_users_pdf(users, config):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    start_y = draw_header(pdf, config)
    y = start_y

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, 690, "Listado de Usuarios")

    data = [["ID", "Email", "Rol", "Verificado"]]
    for u in users:
        data.append([
            str(u.id),
            u.email,
            u.role.name,
            "Sí" if u.is_verified else "No"
        ])

    table = Table(data, colWidths=[60, 200, 120, 80])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkgray),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,0), 8),
        ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
        ("GRID", (0,0), (-1,-1), 0.5, colors.gray)
    ]))

    table.wrapOn(pdf, 40, 600)
    table.drawOn(pdf, 40, 600 - (20 * len(data)))

    pdf.showPage()
    pdf.save()
    buffer.seek(0)

    return buffer
