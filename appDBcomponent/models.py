from django.db import models


class InfoUsers(models.Model):
    name = models.CharField(
        verbose_name="Имя",
        max_length=100,
        null=False,
        blank=False
    )
    age = models.IntegerField(
        verbose_name="Возраст",
        null=True,
        blank=True
    )
    balance = models.FloatField(
        verbose_name="Баланс",
        null=True,
        blank=True,
        default=0.0
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,
        blank=True
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "Доп. инф. пользователей"
