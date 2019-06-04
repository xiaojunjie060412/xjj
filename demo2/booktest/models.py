from django.db import models

# Create your models here.

# 继承models.Model的父类ORM功能
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField()


class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    # book作为外键关联bookinfo表
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
