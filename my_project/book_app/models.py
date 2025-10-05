from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')
    author = models.CharField(max_length=100, verbose_name='author')
    photo = models.ImageField(upload_to='book_photos', verbose_name='photo')

    def __str__(self):
        return f"{self.title} by {self.author}"
