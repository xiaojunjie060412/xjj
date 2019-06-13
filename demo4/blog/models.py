from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Classify(models.Model):
    """
    分类：与文章一对多关系
    title:分类标题
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    标签：与文章多对多关系
    title:标签标题
    """
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    文章：与分类多对一，与标签多对多，与评论一对多
    title:文章标题
    classify:文章分类
    tag:文章标签
    create_time:增加时间
    last_time:最后一次更新时间
    author:文章作者
    read:阅读数
    content:文章内容
    comment:评论数
    """
    title = models.CharField(max_length=20)
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    create_time = models.DateTimeField(auto_now=True)
    last_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return self.title
