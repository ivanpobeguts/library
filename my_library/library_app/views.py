from django.template import RequestContext

from .models import Book
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

import logging


logger = logging.getLogger(__name__)


@login_required(redirect_field_name='/library/')
def index(request):
    books_list = Book.objects.all()
    context = {'books_list': books_list}
    return render(request, 'library/index.html', context)


@login_required(redirect_field_name='/library/')
def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'library/book.html', context)


@login_required(redirect_field_name='/library/')
def add_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    logger.info(user)
    user.books.add(book)
    return redirect('/library/books/' + str(book_id) + '/')


@login_required(redirect_field_name='/library/')
def user(request):
    return render(request, 'user/user.html')


@login_required(redirect_field_name='/library/')
def remove_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    user = request.user
    user.books.remove(book)
    return redirect('/library/user/')
