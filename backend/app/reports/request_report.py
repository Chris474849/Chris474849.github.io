# app/reports/request_report.py
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from app.reports.helpers import draw_header

styles = getSampleStyleSheet()
normal = styles["Normal"]

def build_requests_pdf(requests, config):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    start_y = draw_header(pdf, config)
    y = start_y


    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(40, 690, "Listado de Solicitudes")

    # Encabezados
    data = [["ID", "Nombre", "Email", "Servicio", "Fecha", "Personal", "Teléfono", "Mensaje"]]

    # Filas
    for req in requests:
        data.append([
            req.id,
            Paragraph(req.nombre, normal),
            Paragraph(req.email, normal),
            Paragraph(req.servicio, normal),
            req.fecha.strftime("%Y-%m-%d"),
            Paragraph(req.personal, normal),
            req.telefono,
            Paragraph(req.mensaje, normal)
        ])

    # ===========================================
    # 📌 Cálculo automático de anchos de columna
    # ===========================================
    total_width = 530  # ancho útil de una carta con márgenes
    min_widths = [30, 70, 110, 80, 60, 80, 60, 140]  # base proporcional

    total_min = sum(min_widths)
    scale = total_width / total_min

    colWidths = [w * scale for w in min_widths]

    # ===========================================
    # 📌 Tabla con wrapping habilitado
    # ===========================================
    table = Table(data, colWidths=colWidths)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.darkgray),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("ALIGN", (0,0), (-1,0), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("GRID", (0,0), (-1,-1), 0.4, colors.gray),
        ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),
    ]))

    # ===========================================
    # 📌 Dibujar tabla con ajuste vertical
    # ===========================================
    table.wrapOn(pdf, 40, 600)
    table_height = table._height

    y_position = 680 - table_height
    if y_position < 40:
        pdf.showPage()
        start_y = draw_header(pdf, config)
        y = start_y


    table.drawOn(pdf, 40, y_position)

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer
