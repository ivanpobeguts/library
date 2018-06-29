from django.urls import re_path, path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^book/',  views.book, name='book'),
]
