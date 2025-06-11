from django.urls import path
from .views import helloApi, booksAPI, bookAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins, BooksAPIGenerics, BookAPIGenerics

from rest_framework import routers
from .views import BooksViewSet

# urlpatterns = [
#     path("hello/", helloApi),

#     path("fbv/books/", booksAPI),
#     path("fbv/book/<int:bid>/", bookAPI),

#     path("cbv/books/", BooksAPI.as_view()),
#     path("cbv/book/<int:bid>/", BookAPI.as_view()),

#     path("mixin/books/", BooksAPIMixins.as_view()),
#     path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),

#     path("generics/books/", BooksAPIGenerics.as_view()),
#     path("generics/book/<int:bid>/", BookAPIGenerics.as_view()),
# ]

router = routers.SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = router.urls