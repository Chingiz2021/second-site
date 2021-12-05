from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.db.models import Sum
from django.contrib.contenttypes.fields import GenericRelation

class TypesItem(models.Model):
    id = models.IntegerField('Артикул вещи',primary_key=True)
    title = models.CharField('Тип вещи', max_length=255,null=True)
    price =  models.DecimalField('Цена', max_digits=8, decimal_places=2,null=True)

    def __str__(self):
        return f' артикул вещи : {self.id},\n  наименование: {self.title},\n  цена : {self.price} тг' 

    class Meta:
        
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class Orders(models.Model):
    id = models.IntegerField('Артикул заявки',primary_key=True)
    name = models.CharField('Имя клиента', max_length=255,null=True)
    phone = models.CharField('Номер телефона клиента', max_length=255, null=True)
    email = models.CharField('Email клиента', max_length=255, null=True)
    type = models.TextField('Указан тип вещей', max_length=1000, null=True, help_text='тип вещей указынный клиентом')
    typevesch = models.ForeignKey(TypesItem, verbose_name='Товар', on_delete=models.CASCADE)
    prosmotr = models.BooleanField('Заявка просмотрена ', default=False, help_text='просмотрена ли заявка?')
    obrabotka = models.BooleanField('Заявка обработана ', default=False, help_text='обработана  ли заявка?')
    obrabotka_scklad = models.BooleanField('Уже на складе', default=False, help_text='Вещи по заявке на складе?')
    obrabotka_end = models.BooleanField('Заявка закрыта', default=False, help_text='Заявка обрабатона и в архиве?')
    created = models.DateTimeField('Дата создания заявки',auto_now=True, auto_now_add=False)
    data_succes = models.DateTimeField('Дата когда нужно забрать вещи',null=True)
    
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



class Commands(models.Model):
    name_user = models.CharField('Имя клиента', max_length=255)
    message_text = models.TextField('сообщение от клиента', max_length=1000, null=True, help_text='сообщение от клиента')
    phone = models.CharField('Телефонный номер клиента', max_length=255)
    created = models.DateTimeField('Дата создания комментария',auto_now=True, auto_now_add=False)
    prosmotr = models.BooleanField('Заявка просмотрена ', default=False, help_text='просмотрена ли заявка?')
    def __str__(self):
        return self.name_user



    class Meta:
        
        verbose_name = 'Хочу в команду'
        verbose_name_plural = 'Хотят в команду'
