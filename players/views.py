from django.shortcuts import render
from django.http import Http404
from rest_framework import generics, views, response, status

from .serializers import PlayerSerializer
from .models import Player

# Create your views here.


class PlayerList(generics.ListAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()


class PlayerDetails(views.APIView):
    def get_object(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        player = self.get_object(pk)
        serializer = PlayerSerializer(player)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
