# Generated by Django 3.2.9 on 2021-12-05 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_orders_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
