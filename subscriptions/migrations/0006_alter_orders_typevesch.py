# Generated by Django 3.2.9 on 2021-12-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_alter_orders_data_succes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='typevesch',
            field=models.ManyToManyField(blank=True, to='subscriptions.TypesItem', verbose_name='Вещи в заявке'),
        ),
    ]
