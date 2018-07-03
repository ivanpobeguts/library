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


@login_required(redirect_field_name='/library/')
def book(request, book_id):
    # book_id = request.GET.get('id', '')
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'library/book.html', context)
