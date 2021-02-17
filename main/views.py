from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Games
from .serializers import GameSerializer


# Create your views here.
class GamesList(APIView):
    def get(self, request):
        bicycles = Games.objects.all()
        serializer = GameSerializer(bicycles, many=True)
        return Response({"games": serializer.data})


class GameDetails(APIView):
    def get_object(self, game_id):
        return get_object_or_404(Games, pk=game_id)

    def get(self, request, game_id):
        game = self.get_object(game_id)
        serializer = GameSerializer(game)
        return Response(serializer.data)
