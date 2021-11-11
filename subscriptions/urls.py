from django.urls import path, include

from .views import (
                   create_orders,
                   home_page
                   )


# app_name = 'products'

urlpatterns = [

    path('orders/', include(([
        path('', create_orders, name='create'),
    ], 'orders'), namespace='orders')),
    path('', home_page, name='home_page'),
]