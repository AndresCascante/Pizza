from django.urls import path

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
