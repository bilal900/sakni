from django.contrib import admin

# Register your models here.
from .models import post,Category

admin.site.register(post)
admin.site.register(Category)