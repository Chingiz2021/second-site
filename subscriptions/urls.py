from django.urls import path, include

from .views import (
                   create_orders,
                   home_page,
                   page_oferta,
                   page_sotrudnicestfo,
                   RobotsTxtView,
                   SitemapXmlView,
                   )


# app_name = 'products'

urlpatterns = [

    path('orders/', include(([
        path('', create_orders, name='create'),
    ], 'orders'), namespace='orders')),
    path('', home_page, name='home_page'),
    path('oferta', page_oferta, name='oferta'),
    path('sotrudnicestfo',  page_sotrudnicestfo, name='sotrudnicestfo'),
    path('robots.txt', RobotsTxtView.as_view()),
    path('sitemap.xml', SitemapXmlView.as_view()),
]