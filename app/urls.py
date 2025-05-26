from django.urls import path
from .views import helloApi, booksAPI, bookAPI

urlpatterns = [
    path("hello/", helloApi),
    path("fbv/books", booksAPI),
    path("fbv/book/<int:bid>", bookAPI),
]