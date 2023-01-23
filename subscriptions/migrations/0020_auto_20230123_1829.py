# Generated by Django 3.2.9 on 2023-01-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_alter_cont_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ipuser',
            field=models.CharField(max_length=255, null=True, verbose_name='Ip адресс клиента'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заявки'),
        ),
    ]