from datetime import date
from email.message import EmailMessage
from pydantic import EmailStr
from app.config import settings


def create_booking_confirmation_template(
        booking: dict,
        email_to: EmailStr
):
    email = EmailMessage()

    email["Subject"] = "Подтверждение бронирования"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Подтверждение бронирования</h1>
            Вы забронировали отлель с {booking["date_from"]} по {booking["date_to"]}
        """,
        subtype="html"
    )

    return email

def create_booking_notification_template(
        email_to: EmailStr,
        date_from: date,
        date_to: date
):
    email = EmailMessage()

    email["Subject"] = "У вас завтра заселение"
    email["From"] = settings.SMTP_USER
    email["To"] = email_to

    email.set_content(
        f"""
            <h1>Напоминание о бронировании</h1>
            Вы бронировали отель с {date_from} по {date_to}
        """,
        subtype="html"
    )

    return email