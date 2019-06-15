from django.conf.urls import url
from .views import IndexView, SingleView, ArchivesView, ClassifyView, TagView
from .feed import ArticleFeed

app_name = 'blog'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^single/(\d+)/$', SingleView.as_view(), name='single'),
    url(r'^archives/(\d+)/(\d+)/$', ArchivesView.as_view(), name='archives'),
    url(r'^classify/(\d+)/$', ClassifyView.as_view(), name='classify'),
    url(r'^tag/(\d+)/$', TagView.as_view(), name='tag'),
    url(r'^rss/$', ArticleFeed(), name='rss')
]