import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from .models import  Orders

def send_message_mail(email,message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Оформление заказа"
    msg['From'] = 'second@2nd.kz'
    msg['To'] = email
    part2 = MIMEText(message, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.mail.ru', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('second@2nd.kz', os.getenv('PASSWORD_MAIL'))
    mail.sendmail('second@2nd.kz', email, msg.as_string())
    mail.quit()

@csrf_exempt 
def create_orders(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        order = Orders.objects.create(
                name = data['name'],
                phone = data['phone'],
                email = data['email']
                )
        send_message_mail(data['email'],'Заявка успешно принята')
        send_message_mail('second@2nd.kz','Новая заявка на сайте')
        return JsonResponse({'message': True})

    if request.method == 'GET':
        return JsonResponse({'message': 'ok'})

def home_page(request):
    return render(request, 'index.html')

def page_oferta(request):
    return render(request, 'oferta.html')

def page_sotrudnicestfo(request):
    return render(request, 'sotrudnicestfo.html')


class RobotsTxtView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'


class SitemapXmlView(TemplateView):
    template_name = 'sitemapxml.html'
    content_type = 'application/xml'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context






