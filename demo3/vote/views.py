from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Problem, Answer
from django.views.generic import View
# Create your views here.


def checklogin(fun):
    def check(self, req, *args):
        # if req.COOKIES.get("username"):
        if req.session.get('username'):
            return fun(self, req, *args)
        else:
            return redirect(reverse("vote:login"))
    return check


class ListViews(View):

    @checklogin
    def get(self, req):
        problems = Problem.objects.all()
        return render(req, 'vote/list.html', locals())


class DetailViews(View):

    @checklogin
    def get(self, req, id):
        problem = Problem.objects.get(pk=id)
        return render(req, 'vote/detail.html', locals())

    @checklogin
    def post(self, req, id):
        a_id = req.POST.get('res')
        a = Answer.objects.get(pk=a_id)
        a.count += 1
        a.save()
        return redirect(reverse('vote:result', args=(id,)))


class ResultViews(View):

    @checklogin
    def get(self, req, id):
        problem = Problem.objects.get(pk=id)
        return render(req, 'vote/result.html', locals())


class LoginViews(View):

    def get(self, req):
        return render(req, 'vote/login.html')

    def post(self, req):
        username = req.POST.get('username')
        password = req.POST.get('password')
        # res = redirect(reverse('vote:list'))
        # res.set_cookie('username', username)
        # return res
        req.session['username'] = username
        return redirect(reverse('vote:list'))
