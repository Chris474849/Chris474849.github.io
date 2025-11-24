# from fastapi import BackgroundTasks
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

# conf = ConnectionConfig(
#     MAIL_USERNAME="noreply@tuservidor.com",
#     MAIL_PASSWORD="clave",
#     MAIL_FROM="noreply@tuservidor.com",
#     MAIL_PORT=587,
#     MAIL_SERVER="smtp.gmail.com",
#     MAIL_STARTTLS=True,
#     MAIL_SSL_TLS=False,
#     USE_CREDENTIALS=True
# )

# async def send_verification_email(email: str, code: str):
#     message = MessageSchema(
#         subject="Código de verificación",
#         recipients=[email],
#         body=f"Tu código de verificación es: {code}",
#         subtype="plain"
#     )
#     fm = FastMail(conf)
#     await fm.send_message(message)
