from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_admin_email_order(name,phone,adress,type):
    html_message = render_to_string('email/send_user_code_order.html', {
        'name': name,
        'phone':phone,
        'adress':adress,
        'type':type,
        })
    message = EmailMessage('info@unwanted.ae', html_message, settings.EMAIL_HOST_USER, ['info@unwanted.ae'],)
    message.content_subtype = 'html'

    message.send()

def send_admin_email_sotrud(name,phone, email, message):
    html_message = render_to_string('email/send_user_sotr.html', {
        'name': name,
        'phone':phone,
        'email':email,
        'message':message,
        })
    message = EmailMessage('info@unwanted.ae', html_message, settings.EMAIL_HOST_USER, ['info@unwanted.ae'],)
    message.content_subtype = 'html'

    message.send()


def send_admin_email_commands2(name, phone, message):
    html_message = render_to_string('email/send_user_command.html', {
        'name': name,
        'phone':phone,
        'message':message,
        })
    message = EmailMessage('info@unwanted.ae', html_message, settings.EMAIL_HOST_USER, ['info@unwanted.ae'],)
    message.content_subtype = 'html'

    message.send()