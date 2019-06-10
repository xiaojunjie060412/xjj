from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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


def deletehero(request, id):
    hero = HeroInfo.objects.get(pk=id)
    hero.delete()
    return HttpResponseRedirect('/detail/%s'%(hero.book.id,))


def deletebook(request, id):
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return HttpResponseRedirect('/list/')


def addhero(request, id):
    book = BookInfo.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'booktest/addhero.html', {'book': book})
    elif request.method == 'POST':
        hero = HeroInfo()
        hero.name = request.POST.get("name")
        hero.content = request.POST.get("content")
        hero.gender = request.POST.get("sex")
        hero.book = book
        hero.save()
        return HttpResponseRedirect('/detail/%s'%(id,))


def addbook(request):
    if request.method == 'GET':
        return render(request, 'booktest/addbook.html', {})
    elif request.method == 'POST':
        book = BookInfo()
        book.title = request.POST.get("title")
        book.pub_date = request.POST.get("pub_date")

        book.save()
        return HttpResponseRedirect('/list/')