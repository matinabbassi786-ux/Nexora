from celery import shared_task
import time
import logging

logger = logging.getLogger(__name__)

@shared_task
def test_background_task(user_email):
    logger.info("")
    logger.info(f"Starting email dispatch to {user_email}...")
    time.sleep(5)  # Simulating a slow network or SMTP call
    logger.info(f"Email successfully sent to {user_email}!")
    return f"Sent to {user_email}"
