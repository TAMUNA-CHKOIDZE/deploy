from django.urls import path

from book_app.views import book_list

urlpatterns = [
    path('', book_list, name='books'),
]
