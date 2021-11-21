from django.db import models
from django.urls import reverse

from django.contrib.contenttypes.fields import GenericRelation


class Orders(models.Model):
    name = models.CharField('Имя клиента', max_length=255)
    phone = models.CharField('Номер телефона клиента', max_length=255, null=True)
    email = models.CharField('Email клиента', max_length=255, null=True)
    type = models.TextField('Указан тип вещей', max_length=1000, null=True, help_text='тип вещей указынный клиентом')
    prosmotr = models.BooleanField('Заявка просмотрена ', default=False, help_text='просмотрена ли заявка?')
    obrabotka = models.BooleanField('Заявка обработана ', default=False, help_text='обработана  ли заявка?')
    obrabotka_scklad = models.BooleanField('Уже на складе', default=False, help_text='Вещи по заявке на складе?')
    obrabotka_end = models.BooleanField('Заявка закрыта', default=False, help_text='Заявка обрабатона и в архиве?')
    created = models.DateTimeField('Дата создания заявки',auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.email



    class Meta:
        
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявки'


class Works(models.Model):
    name = models.CharField('Имя клиента', max_length=255)
    phone = models.CharField('Номер телефона клиента', max_length=255, null=True)
    email = models.CharField('Email клиента', max_length=255, null=True)
    message = models.TextField('сообщение от клиента', max_length=1000, null=True, help_text='сообщение от клиента')
    prosmotr = models.BooleanField('Заявка просмотрена ', default=False, help_text='просмотрена ли заявка?')
    created = models.DateTimeField('Дата создания заявки',auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.email



    class Meta:
        
        verbose_name = 'Заявку на сотрудничество'
        verbose_name_plural = 'Заявки на сотрудничество'


class Comments(models.Model):
    name_user = models.CharField('Имя клиента', max_length=255)
    message_text = models.TextField('сообщение от клиента', max_length=1000, null=True, help_text='сообщение от клиента')
    moderation = models.BooleanField('Комментарий допущен?', default=False, help_text='Комментарий допущен?')
    created = models.DateTimeField('Дата создания комментария',auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return self.name_user



    class Meta:
        
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
