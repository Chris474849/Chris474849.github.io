import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 587
SMTP_USER = "dannyfiallo60@gmail.com"
SMTP_PASSWORD = "danny60fiallo"

def send_mail(to, subject, body):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, to, msg.as_string())

def send_verification_email(email, code):
    html = f"""
    <html>
    <body>
        <h2>Verificación de Cuenta</h2>
        <p>Tu código de verificación es:</p>
        <h1>{code}</h1>
        <p>Este código expira en 10 minutos.</p>
    </body>
    </html>
    """
    send_mail(email, "Código de verificación", html)
