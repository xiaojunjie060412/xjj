from django.conf.urls import url
from .views import list, detail, result
app_name = 'vote'

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^detail/(\d+)/$', detail, name='detail'),
    url(r'^result/(\d+)/$', result, name='result'),
]