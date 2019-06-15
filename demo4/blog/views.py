from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from .models import Article, Classify, Tag
from comment.forms import CommentForm
from django.core.paginator import Paginator
import markdown
from comment.models import Comment

# Create your views here.


class IndexView(View):

    def get(self, req):
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