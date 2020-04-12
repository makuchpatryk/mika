from django.contrib import admin

# Register your models here.
from .models import Category, Post, Album, Song

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(Song)
