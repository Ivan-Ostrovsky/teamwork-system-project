from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    position = models.CharField(max_length=100, null=True, blank=True, verbose_name="должность")
    user_pic = models.ImageField(default = "default.jpg", upload_to="media/", blank=True, null=True)
    info = models.TextField(blank=True, null=True)

# Create your models here.
