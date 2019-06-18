from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from .models import Article, Classify, Tag
from comment.forms import CommentForm
from django.core.paginator import Paginator
import markdown
from django.core.mail import send_mail, EmailMultiAlternatives
from comment.models import Comment
from django.http import HttpResponse
from demo4 import settings
from django.views.decorators.cache import cache_page


# Create your views here.


class IndexView(View):

    def get(self, req):
        pass
# @cache_page(60*5)
def index(req):
        article = Article.objects.all()

        pagenum = req.GET.get('page')
        paginator = Paginator(article, 1)
        pagenum = 1 if pagenum == None else pagenum

        page = paginator.get_page(pagenum)
        page.has_previous()
        page.path = '/'
        # print(paginator.count)
        # print(paginator.num_pages)
        # print(paginator.object_list)
        # print(paginator.page_range)
        # page = paginator.get_page(3)
        # print(page.object_list)
        return render(req, 'blog/index.html', {'page': page})


class SingleView(View):

    def get(self, req, id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        article.content = md.convert(article.content)
        article.toc = md.toc
        return render(req, 'blog/single.html', locals())

    def post(self, req, id):
        cf = CommentForm(req.POST)
        if cf.is_valid():
            c = cf.save(commit=False)
            c.article = get_object_or_404(Article, pk=id)
            c.save()
        # name = req.POST.get('name')
        # email = req.POST.get('email')
        # url = req.POST.get('url')
        # content = req.POST.get('content')
        #
        # comment = Comment()
        # comment.name = name
        # comment.email = email
        # comment.url = url
        # comment.content = content
        # comment.article = get_object_or_404(Article, pk=id)
        # comment.save()
        return redirect(reverse('blog:single', args=(id,)))


class ArchivesView(View):

    def get(self,req, year, month):
        article = Article.objects.filter(create_time__year=year, create_time__month=month)
        pagenum = req.GET.get('page')
        paginator = Paginator(article, 1)
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/archives/%s/%s/' % (year, month)
        return render(req, 'blog/index.html', {'page': page})


class ClassifyView(View):

    def get(self, req, id):
        article = Article.objects.filter(classify=(get_object_or_404(Classify, id=id)))
        pagenum = req.GET.get('page')
        paginator = Paginator(article, 1)
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/classify/%s/' % (id,)
        return render(req, 'blog/index.html', {'page': page})


class TagView(View):

    def get(self, req, id):
        article = Article.objects.filter(tag=(get_object_or_404(Tag, id=id)))
        pagenum = req.GET.get('page')
        paginator = Paginator(article, 1)
        pagenum = 1 if pagenum == None else pagenum
        page = paginator.get_page(pagenum)
        page.path = '/tag/%s/' % (id,)
        return render(req, 'blog/index.html', {'page': page})


class ContactView(View):

    def get(self, req):
        return render(req, 'blog/contact.html')


class SendEmailView(View):

    def get(self, req):
        # send_mail("测试邮件html格式",
        #           "<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>",
        #           settings.DEFAULT_FROM_EMAIL,
        #           ["xjj060412@163.com"])
        try:
            mail = EmailMultiAlternatives(subject="测试邮件html格式",
                                          body="<h1>  <a href = 'http://www.baidu.com'> 百度 </a>  </h1>",
                                          from_email=settings.DEFAULT_FROM_EMAIL,
                                          to=["xjj060412@163.com"])
            mail.content_subtype = "html"
            mail.send()

            return HttpResponse('发送成功')
        except:
            return HttpResponse('发送失败')