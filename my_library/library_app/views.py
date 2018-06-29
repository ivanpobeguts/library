from django.template import RequestContext

from .models import Book
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required(redirect_field_name='/library/')
def index(request):
    books_list = Book.objects.all()
    context = {'books_list': books_list}
    return render(request, 'library/index.html', context)


# def login(request):
#     if request.method == "GET":
#         return render(request, 'library/login.html')
#     elif request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             auth.login(request, user)
#             return redirect('index')
#         else:
#             pass
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect("/library/logout/")
