from django.db import models

# Create your models here.

class ChatUser(models.Model):
    chat_id = models.CharField('Id пользователя телеграм',max_length=255)
    full_name = models.CharField('Никнейм пользователя телеграм',max_length=255)
    active = models.BooleanField('Может ли получать заявки',default=False)

    class Meta:
      
        ordering = ["-id"]
        verbose_name = "Пользователь бота телеграмм"
        verbose_name_plural = "Пользователи бота телеграмм"

    def __str__(self) -> str:
        return self.full_name or str(self.chat_id)