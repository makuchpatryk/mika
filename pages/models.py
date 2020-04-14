from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Hashtag(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")

    def __str__(self):
        return self.title

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Title")
    image = models.ImageField(upload_to ='uploads/', blank=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    yt_link = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})


class Album(models.Model):
    album_name = models.CharField(max_length=250)
    album_picture = models.ImageField(upload_to ='uploads/', blank=True)
    description = models.CharField(max_length=250)
    ctime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.get_username() + ' - ' + self.album_name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    cover = models.ImageField(upload_to ='uploads/', blank=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    song_name= models.CharField(max_length=1000)
    description = models.CharField(max_length=250)

    def __str__(self):
        return  self.song_name


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    ctime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
