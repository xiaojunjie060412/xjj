from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import BookInfo, HeroInfo

# Create your views here.


def index(request):
    # temp = loader.get_template('booktest/index.html')
    # res = temp.render({})
    #
    # return HttpResponse(res)
    return render(request, 'booktest/index.html', {})


def list(request):
    books = BookInfo.objects.all()
    # temp = loader.get_template('booktest/list.html')
    # res = temp.render({'books': books})
    #
    # return HttpResponse(res)
    return render(request, 'booktest/list.html', {'books': books})


def detail(request, id):
    book = BookInfo.objects.get(pk=id)
    # temp = loader.get_template('booktest/detail.html')
    # res = temp.render({'book': book})
    #
    # return HttpResponse(res)
    return render(request, 'booktest/detail.html', {'book': book})
