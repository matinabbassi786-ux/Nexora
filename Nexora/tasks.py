import time
from celery import shared_task
import logging
from datetime import datetime


logger = logging.getLogger(__name__)


@shared_task
def send_notification(student_id, message):
    student_id  = student_id *2
    logger.info("=====================")
    logger.info("Student ID: %s", student_id)

    logger.info("Message: %s", message)
    logger.info("=====================")

    return "Notification sent"


@shared_task
def test_schedule():

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"NEXORA SCHEDULE EXECUTED: {now}", flush=True)

    return {
        "status": "SUCCESS",
        "executed_at": now
    }