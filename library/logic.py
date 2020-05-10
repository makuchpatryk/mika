from pages import models
from . import exceptions
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


def create_order_payment(payload):
    try:
        order = models.OrderPayment()
        order.email = payload['email']
        order.transation_id = payload['transation_id']

        order.surname = payload.get('surname', '')

        order.address_1 = payload.get('address_1', '')
        order.address_2 = payload.get('address_2', '')

        order.city = payload.get('city', '')
        order.state = payload.get('state', '')
        order.postcode = payload.get('postcode', '')
        order.number = payload.get('number', '')

        order.status = models.Order.ORDERED
        order.save()
    except Exception as e:
        raise exceptions.MikaException(e)
    return order.pk


def get_post_by_uid(pk):
    try:
        post = models.Post.objects.get(pk=pk)
    except ObjectDoesNotExist as e:
        raise exceptions.MikaException(e)
    return post


def like_post(pk):
    try:
        post = models.Post.objects.get(pk=pk)
        like = models.Like()
        like.post = post
        like.save()
    except ObjectDoesNotExist as e:
        raise exceptions.MikaException(e)

    return like


def comment_post(**kwargs):
    post = get_post_by_uid(kwargs['post_id'])
    try:
        comment = models.Comment()
        comment.post = post
        comment.content = kwargs['content']
        comment.name = kwargs['name']
        comment.save()
    except Exception as e:
        raise exceptions.MikaException(e)

    return comment
