from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from .models import Article
from comment.forms import CommentForm
from comment.models import Comment

# Create your views here.


class IndexView(View):

    def get(self, req):
        article = Article.objects.all()
        return render(req, 'blog/index.html', locals())


class SingleView(View):

    def get(self, req, id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm()
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