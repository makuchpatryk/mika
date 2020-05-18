import json

from django import template
from pages import models
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag('tags/blog/other_posts.html')
def other_posts(limit=5):
    posts = models.Post.objects.all().order_by('?')[:limit]
    context = {'posts': posts}
    return context

@register.filter(name='jsonify')
def jsonify(value):
    return json.dumps(value)

@register.filter(name='split')
def split(str, key):
    return str.split(key)

@register.filter
def get_by_index(a, i):
    return a[i]
