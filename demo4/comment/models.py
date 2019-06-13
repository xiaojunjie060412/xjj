from django.db import models
from blog.models import Article
# Create your models here.


class Comment(models.Model):
    """
    评论：与文章多对一
    comment:评论内容
    article:所属文章
    """
    name = models.CharField(max_length=20, verbose_name='名字')
    create_time = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    url = models.URLField(null=True, blank=True, verbose_name='地址')
    content = models.CharField(max_length=500, verbose_name='内容')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


