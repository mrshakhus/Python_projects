from celery import Celery
from celery.schedules import crontab
from app.config import settings



celery = Celery(
    "tasks",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    include=[
        "app.tasks.tasks",
        "app.tasks.scheduled"
    ]
)

celery.conf.beat_schedule = {
    "any_name": {
        "task": "tomorrow_check_in",
        "schedule": 5 #seconds
        # "schedule": crontab(minute="0", hour="9")
    }
}