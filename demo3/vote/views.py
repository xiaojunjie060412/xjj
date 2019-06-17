from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Problem, Answer, MyUser
from django.views.generic import View
from .forms import MyUserLoginForm, MyUserRegistForm
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMultiAlternatives
from itsdangerous import TimedJSONWebSignatureSerializer
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import random, io
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
        verify = req.POST.get('verify')
        # user = authenticate(req, username=username, password=password)
        user = MyUser.objects.filter(username=username)
        if user:
            if user[0].check_password(password):
                if user[0].is_active:
                    if verify == req.session.get('verifycode'):

                        user1 = authenticate(req, username=username, password=password)
                        login(req, user1)
                        return redirect(reverse('vote:list'))
                    else:
                        lf = MyUserLoginForm()
                        rf = MyUserRegistForm()
                        errormessage = '验证码错误'
                        return render(req, 'vote/login.html', locals())
                else:
                    lf = MyUserLoginForm()
                    rf = MyUserRegistForm()
                    errormessage = '用户尚未激活'
                    return render(req, 'vote/login.html', locals())
            else:
                lf = MyUserLoginForm()
                rf = MyUserRegistForm()
                errormessage = '密码错误'
                return render(req, 'vote/login.html', locals())

        else:
            lf = MyUserLoginForm()
            rf = MyUserRegistForm()
            errormessage = '用户名不存在'
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
            user.is_active = False
            user.save()
            userid = user.id
            from django.conf import settings
            util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
            userid = util.dumps({'userid': userid}).decode('utf-8')
            info = '请激活<a href="http://127.0.0.1:8000/active/%s/"> 点我激活%s</a>' % (userid, username,)
            from django.conf import settings
            mail = EmailMultiAlternatives("请激活", info, settings.DEFAULT_FROM_EMAIL, [email])
            mail.content_subtype = 'html'
            mail.send()
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


class ActiveView(View):

    def get(self, req, id):

        util = TimedJSONWebSignatureSerializer(secret_key=settings.SECRET_KEY)
        obj = util.loads(id)
        id = obj['userid']
        user = MyUser.objects.filter(pk=id).first()
        if user:
            user.is_active = True
            user.save()
            return redirect(reverse('vote:login'))


class CheckUsernameView(View):

    def get(self, req):
        username = req.GET.get('username')
        user = MyUser.objects.filter(username=username).first()
        if user:
            return JsonResponse({'statecode': 1})
        else:
            return JsonResponse({'statecode': 0, 'error': '用户名不存在'})


class VerifyView(View):

    def get(self, req):

        # 定义变量，用于画面的背景色、宽、高
        bgcolor = (random.randrange(20, 100),
                   random.randrange(20, 100),
                   random.randrange(20, 100))
        width = 100
        heigth = 25
        # 创建画面对象
        im = Image.new('RGB', (width, heigth), bgcolor)
        # 创建画笔对象
        draw = ImageDraw.Draw(im)

        # 调用画笔的point()函数绘制噪点
        for i in range(0, 100):
            xy = (random.randrange(0, width), random.randrange(0, heigth))
            fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
            draw.point(xy, fill=fill)

        # 定义验证码的备选值
        str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
        # 随机选取4个值作为验证码
        rand_str = ''
        for i in range(0, 4):
            rand_str += str1[random.randrange(0, len(str1))]
        # 构造字体对象
        font = ImageFont.truetype('calibrib.ttf', 23)
        fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
        draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
        draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
        draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
        # 释放画笔
        del draw
        req.session['verifycode'] = rand_str
        f = io.BytesIO()
        im.save(f, 'png')
        # 将内存中的图片数据返回给客户端，MIME类型为图片png
        return HttpResponse(f.getvalue(), 'image/png')