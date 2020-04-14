from django.contrib import admin

# Register your models here.
from .models import Category, Post, Album, Song, Hashtag, Order


class AlbumAdmin(admin.ModelAdmin):
    fields = ('album_name', 'album_picture', 'ctime', 'description', 'author')



class SongAdmin(admin.ModelAdmin):
    fields = ('album', 'cover', 'ctime', 'song_name', 'description')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('email', 'ctime', 'done')
    readonly_fields = ['ctime']


admin.site.register(Category)
admin.site.register(Post)

admin.site.register(Order, OrderAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)

admin.site.register(Hashtag)