from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
from .models import Category, Post, Album, Song, Hashtag, Order, OrderPayment, Like


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'ctime', 'description', 'author')



class SongAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'album', 'ctime', 'description')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('email', 'ctime', 'send_confirmation', 'done')
    readonly_fields = ['ctime']

    def send_confirmation(self, obj):
    	if not obj.done:
		    return format_html(
		    	'<a href="{}?email={}">Wyslij Potwierdzenie</a>&nbsp;',
		    	reverse('sent_confimation', kwargs={'pk': obj.pk}),
				obj.email)


class OrderPaymentAdmin(admin.ModelAdmin):
    list_display = ('email', 'ctime', 'send_confirmation', 'done')
    readonly_fields = ['ctime']

    def send_confirmation(self, obj):
        if not obj.done:
            return format_html(
                '<a href="{}?email={}">Wyslij Potwierdzenie</a>&nbsp;',
                reverse('sent_confimation', kwargs={'pk': obj.pk}),
                obj.email)


admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Like)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderPayment, OrderPaymentAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)

admin.site.register(Hashtag)