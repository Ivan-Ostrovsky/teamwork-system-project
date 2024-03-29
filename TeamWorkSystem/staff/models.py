from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    position = models.CharField(max_length=100, null=True, blank=True, verbose_name="должность")
    user_pic = models.ImageField(default = "default.jpg", upload_to="media/", blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    department = models.ForeignKey('UserDepartament', related_name='worker', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username


class UserDepartament(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name="Назване отдела")
    head = models.ForeignKey(User, on_delete=models.PROTECT)
    super_department = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Departament'

    def __str__(self):
        return self.name

# Create your models here.
