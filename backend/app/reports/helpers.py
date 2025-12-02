# app/reports/helpers.py
from reportlab.lib.pagesizes import letter

HEADER_BOTTOM_Y = 690  # y seguro debajo del encabezado

def draw_header(pdf, config):
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(40, 760, config["hero"]["title"])

    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, 740, config["hero"]["subtitle"])

    pdf.setFont("Helvetica-Oblique", 10)
    pdf.drawString(40, 725, f"{config['siteName']} - {config['footer']['contact']['email']}")

    pdf.line(40, 715, 570, 715)

    return HEADER_BOTTOM_Y
