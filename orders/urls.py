from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(r'^login/$', auth_views.LoginView.as_view(template_name='orders/login.html'), name='login'),
    path(r'^logout/$', auth_views.LogoutView.as_view(next_page='my_login'), name='logout'),
    path(r'^menu/$', views.show_menu, name='menu'),
    #url(r'^signup/$', core_views.signup, name='signup'),
]
