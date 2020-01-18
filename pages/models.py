from django.db import models
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Title")
    text = models.TextField()