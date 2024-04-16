from django.db import models
from staff.models import User
from django.utils.timezone import now


class CorporationNews(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField(default="Text News", blank=False)
    publish = models.DateTimeField(default=now) # учет часовых поясов
    author = models.ForeignKey(User, related_name='News', on_delete=models.PROTECT) # удаляем автора - новости сохраняем
# удаленные сотрудники могут находиться в разных часовых поясах
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['publish']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
    
class NewsComments(models.Model):
    news = models.ForeignKey(CorporationNews, related_name='Comments', on_delete=models.CASCADE) # удаляем новость и коментарии
    comment = models.TextField(blank=False)
    date = models.DateTimeField(default=now)
    writer = models.ForeignKey(User, related_name='Comments', on_delete=models.PROTECT)

    def __str__ (self):
        return 'Comment by {} on {}'.format(self.writer, self.news)
    
    class Meta:
        ordering = ['date']
        verbose_name = 'Коментарии к новостям'
        verbose_name_plural = 'Коментарии к новостям'


# Create your models here.
