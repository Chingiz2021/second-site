# Generated by Django 3.2.9 on 2021-12-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20211205_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='typevesch',
            field=models.ManyToManyField(blank=True, to='subscriptions.TypesItem', verbose_name='Товар'),
        ),
    ]