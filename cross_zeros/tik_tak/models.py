from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    """
    Current user
    """
    photo = models.ImageField(
        upload_to="pictures/",
        default="no_photo.png",
        verbose_name="Фото користувача",
    )

    phone = models.CharField(max_length=15, verbose_name="Номер телефона", default="", blank=True, null=True)

    # REQUIRED_FIELDS = ["email", "username"]


class Message(models.Model):
    """
    Message
    """
    text_message = models.TextField(verbose_name="Текст повідомлення")
    from_user = models.ForeignKey(
        MyUser, verbose_name="Отримувач", on_delete=models.DO_NOTHING, related_name="username_from"
    )
    to_user = models.ForeignKey(
        MyUser, verbose_name="Відправник", on_delete=models.DO_NOTHING, related_name="username_to"
    )
    date_send_message = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")

    def __str__(self):
        return f"{self.from_user} to {self.to_user}"

    class Meta:
        verbose_name = "Повідомлення"
        verbose_name_plural = "Повідомлення"
