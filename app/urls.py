from django.urls import path
from .views import helloApi, booksAPI, bookAPI, BookAPI, BooksAPI

urlpatterns = [
    path("hello/", helloApi),
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
]