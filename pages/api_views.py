from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache


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
