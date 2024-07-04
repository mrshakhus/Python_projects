from datetime import datetime, timezone
import smtplib
from pydantic import EmailStr
from app.tasks.celery import celery
from app.tasks.dao import BookingTaskDAO
from app.tasks.email_templates import create_booking_notification_template
from app.config import settings

@celery.task(name="tomorrow_check_in")
def send_notification_1_day_email(
    # booking: dict,
    email_to: EmailStr
):
    """
    Таска будет напоминать о бронировании тем пользователям, у кого на завтра запланирован заезд в отель. Таска/функция должна выполняться каждый день в 9 утра (задайте через crontab)
    """
    users = BookingTaskDAO.get_day_before_users(datetime.now(timezone.utc))
    print(datetime.now(timezone.utc))
    print(users)

    for user in users:
        msg_content = create_booking_notification_template( email_to)

        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
            server.send_message(msg_content)