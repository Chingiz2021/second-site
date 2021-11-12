import json

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

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
        return JsonResponse({'message': True})

    if request.method == 'GET':
        return JsonResponse({'message': 'ok'})

def home_page(request):
    return render(request, 'index.html')

