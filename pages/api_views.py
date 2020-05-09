from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from rest_framework import status

from library import utils, logic, exceptions

from . import forms


class MusicPlayView(APIView):
    def get(self, request):
        return Response({})

    def post(self, request, *args, **kwargs):
        cache.delete('music')
        cache.get_or_set('music', True, 60*60)
        print(cache.get('music'))
        return Response({})


class MusicStopView(APIView):
    def get(self, request):
        return Response({})

    def post(self, request, *args, **kwargs):
        cache.delete('music')
        cache.get_or_set('music', False, 60*60)
        print(cache.get('music'))
        return Response({})


class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        data = utils.to_query_dict(
            request.POST if request.POST else request.data)
        form = forms.OrderPaymentForm(data)

        if not form.is_valid():
            return utils.api_res(
                body={"errors": form.errors})

        payload = form.to_payload(data)
        try:
            logic.create_order_payment(payload)
        except exceptions.MikaException as e:
            return utils.api_res(
                body={"errors": e})

        return Response(
            {"message": "ok"},
            status=status.HTTP_201_CREATED)


class likePostView(APIView):
    def post(self, request, *args, **kwargs):
        data = utils.to_query_dict(
            request.POST if request.POST else request.data)

        uid = int(data.get('uid'))
        try:
            logic.like_post(pk=uid)
        except exceptions.MikaException as e:
            return utils.api_res(
                body={"errors": e})

        return Response(
            {"message": "ok"},
            status=status.HTTP_201_CREATED)


class commentPostView(APIView):
    def post(self, request, *args, **kwargs):
        data = utils.to_query_dict(
            request.POST if request.POST else request.data)
        form = forms.CommentPostForm(data)

        if not form.is_valid():
            return utils.api_res(
                body={"errors": form.errors})

        payload = form.to_payload(data)
        try:
            comment = logic.comment_post(**payload)
            emial = form.send_email()
        except exceptions.MikaException as e:
            return utils.api_res(
                body={"errors": e})

        return Response(
            {"message": "ok"},
            status=status.HTTP_201_CREATED)
