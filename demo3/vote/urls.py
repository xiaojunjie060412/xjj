from django.conf.urls import url
from .views import ListViews, DetailViews, ResultViews, LoginViews, \
    RegistViews, LogoutViews, ActiveView, CheckUsernameView, VerifyView
app_name = 'vote'

urlpatterns = [
    url(r'^list/$', ListViews.as_view(), name='list'),
    url(r'^detail/(\d+)/$', DetailViews.as_view(), name='detail'),
    url(r'^result/(\d+)/$', ResultViews.as_view(), name='result'),
    url(r'^login/$', LoginViews.as_view(), name='login'),
    url(r'^regist/$', RegistViews.as_view(), name='regist'),
    url(r'^logout/$', LogoutViews.as_view(), name='logout'),
    url(r'^active/(.*?)/$', ActiveView.as_view(), name='active'),
    url(r'^checkusername/$', CheckUsernameView.as_view(), name='checkusername'),
    url(r'^verify/$', VerifyView.as_view(), name='verify'),
]