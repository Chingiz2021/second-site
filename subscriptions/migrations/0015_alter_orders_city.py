# Generated by Django 3.2.9 on 2021-12-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_auto_20211208_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Город клиента'),
        ),
    ]
