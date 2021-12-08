# Generated by Django 3.2.9 on 2021-12-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_alter_orders_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cont',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counts', models.IntegerField(verbose_name=' Количество посещений')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='За какой месяц')),
            ],
            options={
                'verbose_name': 'Количество просмотров',
                'verbose_name_plural': 'Количество просмотров',
            },
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
