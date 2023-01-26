from email import message
import os
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
from django.core.exceptions import ObjectDoesNotExist
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView

from .models import  Orders, Works, Comments, Commands,Cont
from .email import send_admin_email, send_client_email, send_admin_email_sotr, send_admin_email_commands

@csrf_exempt 
def create_counts(request):
    if request.method == 'POST':
       
       
    #    cont = Cont.objects.save()
        try:
            alls = Cont.objects.get(created__month = datetime.now().month)
            alls.counts = alls.counts +1
            alls.save()
        except ObjectDoesNotExist:
            alls = None
        if not alls:
            test = Cont.objects.create(counts = 1)
        
    return JsonResponse({'message': 'alls'})

def send_message_mail(email,message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "New application"
    msg['From'] = 'info@unwanted.ae'
    msg['To'] = email
    part2 = MIMEText(message, 'html')
    msg.attach(part2)
    mail = smtplib.SMTP('smtp.mail.ru', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('info@unwanted.ae', 'AT8vcbMSdn3idjtJ2bNd')
    mail.sendmail('info@unwanted.ae', email, msg.as_string())
    mail.quit()
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

from .services import send_admin_email_order
@csrf_exempt 
def create_orders(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ip = get_client_ip(request)
        req_ip = Orders.objects.filter(ipuser = str(ip)).first()
        
     
        order = Orders.objects.create(
                name = data['name'],
                phone = data['phone'],
                adress = data['adress'],
                type = data['type'],
                ipuser = str(ip)
                )
        send_admin_email_order(data['name'], data['phone'], data['adress'], data['type'])
        return JsonResponse({'message': True})




def get_price(request):
    if request.method == 'GET':
        data = json.loads(request.body)
        
        order = Orders.objects.get(
                id = data['pk']
        )
        return JsonResponse({'message': order.total})


from .services import send_admin_email_sotrud
@csrf_exempt 
def create_orders_sotrud(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if not  data['message']:
            message = 'not message'
        else:
            message = data['message']
        order = Works.objects.create(
                name = data['name'],
                phone = data['phone'],
                email = data['email'],
                message = message ,
                )
        
        threading.Thread(target=send_admin_email_sotrud, args=((data['name'], data['phone'], data['email'], message))).start()

        
        return JsonResponse({'message': True})

@csrf_exempt 
def create_comments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = Comments.objects.create(
                name_user = data['name_user'],
                message_text = data['message_text'],
                )
        return JsonResponse({'message': True})


from .services import send_admin_email_commands2
@csrf_exempt 
def create_commands(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        commands = Commands.objects.create(
                name_user = data['name_user'],
                message_text = data['message_text'],
                phone = data['phone']
                )
        send_admin_email_commands2(data['name_user'], data['phone'], data['message_text'])
   
        return JsonResponse({'message': True})

def home_page(request):
    comments = Comments.objects.filter(moderation=True)
    context = {
        'comments':comments
    }
    return render(request, 'index.html',context=context)

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






