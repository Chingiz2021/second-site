import json

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

from .models import  Orders

@csrf_exempt 
def create_orders(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        order = Orders.objects.create(
                name = data['name'],
                phone = data['phone'],
                email = data['email']
                )
        send_mail('Subject', 'Заявка принята','second@2nd.kz' , [data['email']])
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






