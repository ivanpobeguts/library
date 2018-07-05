from django.urls import re_path, path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^books/$', views.index, name='index'),
    path('books/<int:book_id>/', views.book, name='book'),
    path('books/<int:book_id>/add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/remove/', views.remove_book, name='remove_book'),
    path('user/', views.user, name='user_page'),
    re_path(r'^accounts/signup/$', views.signup, name='signup'),
]
