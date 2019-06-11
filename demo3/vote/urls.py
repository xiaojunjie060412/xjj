from django.conf.urls import url
from .views import ListViews, DetailViews, ResultViews, LoginViews
app_name = 'vote'

urlpatterns = [
    url(r'^list/$', ListViews.as_view(), name='list'),
    url(r'^detail/(\d+)/$', DetailViews.as_view(), name='detail'),
    url(r'^result/(\d+)/$', ResultViews.as_view(), name='result'),
    url(r'^login/$', LoginViews.as_view(), name='login'),
]