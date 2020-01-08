from rest_framework.views import APIView
from rest_framework.response import Response


class MusicPlayingView(APIView):
    def get(self, request):
        return Response({"articles": []})
