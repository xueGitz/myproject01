from celery import Celery

from django.core.mail import send_mail

app = Celery('hello', broker='redis://192.168.12.155:6379/1')

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

@app.task
def send_email(subject, message, sender, receiver, html_message):
    send_mail(subject, message, sender, receiver, html_message = html_message)