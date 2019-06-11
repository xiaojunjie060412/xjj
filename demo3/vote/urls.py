from django.conf.urls import url
from .views import ListViews, DetailViews, ResultViews
app_name = 'vote'

urlpatterns = [
    url(r'^list/$', ListViews.as_view(), name='list'),
    url(r'^detail/(\d+)/$', DetailViews.as_view(), name='detail'),
    url(r'^result/(\d+)/$', ResultViews.as_view(), name='result'),
]