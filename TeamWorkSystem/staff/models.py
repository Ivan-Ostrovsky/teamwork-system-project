from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    position = models.CharField(max_length=100, null=True, blank=True, verbose_name="должность")
    user_pic = models.ImageField(default = "default.jpg", upload_to="media/", blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    department = models.ForeignKey('UserDepartament', related_name='worker', on_delete=models.PROTECT, null=True, blank=True)
    # related_name записи первичной модели, предназначенного для доступа к связанным записям вторичной модели

    def __str__(self):
        return self.username


class UserDepartament(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Назване отдела")
    head = models.ForeignKey(User, on_delete=models.PROTECT)
    super_department = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True) # обращение модели к себе сомой

    class Meta:
        verbose_name = 'Departament'

    def __str__(self):
        return self.name



@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# у каждого пользователя автоматически сгенерированный токен при регистрации

# Create your models here.
