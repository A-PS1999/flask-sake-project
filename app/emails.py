from flask import render_template, current_app
from flask_mail import Message
from app import mail
from threading import Thread
import os


def async_email(app, msg):
    with app().app_context():
        mail.send(msg)


def send_email(subject, template, recipients, **kwargs):
    sender = os.environ.get("MAIL_USERNAME")

    msg = Message(subject, sender=sender, recipients=[recipients])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    Thread(target=async_email, args=(current_app._get_current_object(), msg)).start()
