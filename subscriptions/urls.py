from django.urls import path, include

from .views import (
                   create_orders,
                   home_page,
                   page_oferta,
                   create_comments,
                   create_orders_sotrud,
                   RobotsTxtView,
                   SitemapXmlView,
                   )


# app_name = 'products'

urlpatterns = [

    path('orders/', include(([
        path('', create_orders, name='create'),
    ], 'orders'), namespace='orders')),
    path('sotrudnichestvo', create_orders_sotrud, name='sotr'),
    path('comment_create', create_comments, name='comment_create'),
    path('', home_page, name='home_page'),
    path('oferta', page_oferta, name='oferta'),
    path('robots.txt', RobotsTxtView.as_view()),
    path('sitemap.xml', SitemapXmlView.as_view()),
]