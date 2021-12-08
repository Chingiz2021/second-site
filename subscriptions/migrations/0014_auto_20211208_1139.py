# Generated by Django 3.2.9 on 2021-12-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0013_delete_typesitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=255, null=True, verbose_name='Город клиента')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=255, null=True, verbose_name='Город клиента'),
        ),
    ]