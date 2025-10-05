from django.contrib import admin
from django.utils.html import format_html

from book_app.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'photo_tag']

    # ადმინში, რომ პატარა ფოტო გამოჩნდეს ატვირთვის შემდეგ
    def photo_tag(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height:auto;" />', obj.photo.url)
        return "-"

    photo_tag.short_description = 'Photo'


admin.site.register(Book, BookAdmin)
