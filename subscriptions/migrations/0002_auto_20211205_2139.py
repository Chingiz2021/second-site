# Generated by Django 3.2.9 on 2021-12-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='typevesch',
        ),
        migrations.AddField(
            model_name='orders',
            name='typevesch',
            field=models.ManyToManyField(to='subscriptions.TypesItem', verbose_name='Товар'),
        ),
    ]
