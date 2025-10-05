from django.contrib import admin
from book_app.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']


admin.site.register(Book, BookAdmin)
