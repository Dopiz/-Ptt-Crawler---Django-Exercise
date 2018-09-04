import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class History(models.Model):
    article_id = models.CharField(max_length=30)
    article_title = models.CharField(max_length=30)
    article_link = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.article_title
