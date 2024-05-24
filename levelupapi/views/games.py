"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game


class GameView(ViewSet):
    """Level up game  view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game 

        Returns:
            Response -- JSON serialized game 
        """
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game 

        Returns:
            Response -- JSON serialized list of game 
        """
        games = Game.objects.all()

        # Add in the next 3 lines
        game_type = request.query_params.get('type', None)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'make', 'gamer', 'number_of_players', 'skill_level')
