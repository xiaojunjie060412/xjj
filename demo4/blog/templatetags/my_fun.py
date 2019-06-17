from django.template import Library
from ..models import Article, Tag, Classify, Ads

register = Library()


@register.simple_tag
def new_article(num=3):
    return Article.objects.order_by('-create_time')[:num]


@register.simple_tag
def getarchives():
    return Article.objects.dates('create_time', 'month')


@register.simple_tag
def getclassify():
    return Classify.objects.all()


@register.simple_tag
def tag():
    return Tag.objects.all()


@register.simple_tag
def getads():
    return Ads.objects.all()