from django.contrib import admin
from .models import Photo # __init__.py가 패키지로 인식하게함
# Register your models here.
admin.site.register(Photo)

