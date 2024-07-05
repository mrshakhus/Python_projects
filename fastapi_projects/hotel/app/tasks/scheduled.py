from datetime import datetime, timezone
import smtplib
from app.tasks.celery import celery
from app.tasks.dao import BookingTaskDAO
from app.tasks.email_templates import create_booking_notification_template
from app.config import settings


async def send_notification_email(days_before_check_in):

    todays_date = datetime.now(timezone.utc).date()
    users = await BookingTaskDAO.get_users_for_notification(todays_date, days_before_check_in)
    await send_notification_email(users)

    for user in users:
        msg_content = create_booking_notification_template(
            user["email"], 
            user["date_from"],
            user["date_to"],
            days_before_check_in
        )

        with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.login(settings.SMTP_USER, settings.SMTP_PASS)
            server.send_message(msg_content)


@celery.task(name="tomorrow_check_in")
async def send_notification_1_day_email():
    """
    Таска будет напоминать о бронировании тем пользователям, у кого на завтра запланирован заезд в отель. Таска/функция должна выполняться каждый день в 9 утра (задайте через crontab)
    """
    send_notification_email(1)


@celery.task(name="in_3_days_check_in")
async def send_notification_3_day_email():
    """
    Вторая таска будет напоминать о бронировании тем пользователям, у кого через 3 дня запланирован заезд в отель. Таска/функция должна выполняться каждый день в 15:30 утра (задайте через crontab)
    """
    send_notification_email(3)

    