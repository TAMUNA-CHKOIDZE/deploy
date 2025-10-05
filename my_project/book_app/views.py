from django.shortcuts import render
from book_app.models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, template_name='book_list.html', context={'books': books})
