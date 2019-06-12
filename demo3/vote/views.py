from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Problem, Answer, MyUser
from django.views.generic import View
from .forms import MyUserLoginForm, MyUserRegistForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def checklogin(fun):
    def check(self, req, *args):
        # if req.COOKIES.get("username"):
        # if req.session.get('username'):
        #     return fun(self, req, *args)
        if req.user and req.user.is_authenticated:
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
        lf = MyUserLoginForm()
        rf = MyUserRegistForm()
        return render(req, 'vote/login.html', locals())

    def post(self, req):

        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(req, username=username, password=password)
        if user:
            login(req, user)
            print('++++++++++++++++++++++')
            return redirect(reverse('vote:list'))
        else:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage = '登录失败'
            return render(req, 'vote/login.html', locals())

        # res = redirect(reverse('vote:list'))
        # res.set_cookie('username', username)
        # return res
        # req.session['username'] = username

        # lf = LoginForm(req.POST)
        # print(lf.is_valid())
        # print(lf.cleaned_data['email'])
        # print(lf.cleaned_data['username'])
        # print(lf.cleaned_data['password'])
        # return redirect(reverse('vote:list'))


class RegistViews(View):

    def get(self, req):
        pass

    def post(self, req):
        try:
            username = req.POST.get('username')
            password = req.POST.get('password')
            email = req.POST.get('email')
            user = MyUser.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect(reverse('vote:login'))

        except:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage = '注册失败'
            return render(req, 'vote/login.html', locals())


class LogoutViews(View):
    def get(self, req):
        logout(req)
        return redirect(reverse('vote:login'))