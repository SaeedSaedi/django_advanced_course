from celery import shared_task
import time


@shared_task
def sendEmail():
    time.sleep(10)
    print("this email sent now")
