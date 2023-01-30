from django.urls import path
# https://evileg.com/ru/forum/topic/1036/

from .views import UpdateBot, UpdateTestBot
urlpatterns = [
    path('', UpdateBot.as_view(), name='update'),
    path('test-message/', UpdateTestBot.as_view(), name='update-bot'),
]