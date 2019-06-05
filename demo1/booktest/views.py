from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo, HeroInfo

# Create your views here.


def index(request):
    temp = loader.get_template('booktest/index.html')
    res = temp.render({})

    return HttpResponse(res)


def list(request):
    books = BookInfo.objects.all()
    temp = loader.get_template('booktest/list.html')
    res = temp.render({'books': books})

    return HttpResponse(res)


def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    temp = loader.get_template('booktest/detail.html')
    res = temp.render({'book': book})

    return HttpResponse(res)
