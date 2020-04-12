from django import template
from pages import models

register = template.Library()

@register.inclusion_tag('tags/blog/other_posts.html')
def other_posts(limit=5):
    posts = models.Post.objects.all().order_by('?')[:limit]
    context = {'posts': posts}
    return context
