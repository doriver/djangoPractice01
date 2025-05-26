from django.urls import path
from .views import helloApi

urlpatterns = [
    path("hello/", helloApi)
]