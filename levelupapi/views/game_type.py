"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import GameType


class GameTypeView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        # Handle GET requests for single game type
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type)
        return Response(serializer.data)
     #  Returns:
        # Response -- JSON serialized game type



    def list(self, request):
        # Handle GET requests to get all game types
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(game_types, many=True)
        return Response(serializer.data)
        
# The Serializer
class GameTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameType
        fields = ('id', 'label')

#The Meta class holds configuration for serializer. We’re telling the serializer to use the GameType model and to include id and label fields.
