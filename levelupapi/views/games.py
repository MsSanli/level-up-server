"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType


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
      
    def create(self, request):
      """Handle POST operations

      Returns
          Response -- JSON serialized game instance
      """
      gamer = Gamer.objects.get(uid=request.data["userId"])
      game_type = GameType.objects.get(pk=request.data["gameType"])

      game = Game.objects.create(
          title=request.data["title"],
          make=request.data["make"],
          number_of_players=request.data["numberOfPlayers"],
          skill_level=request.data["skillLevel"],
          game_type=game_type,
          gamer=gamer,
      )
      serializer = GameSerializer(game)
      return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.make = request.data["make"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]

        game_type = GameType.objects.get(pk=request.data["gameType"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # destroy method like retrieve/update take pk as argument. pk to get the single object, then call the delete from the ORM to remove it from the database.
    def destroy(self, request, pk):
      game = Game.objects.get(pk=pk)
      game.delete()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game
    """
    class Meta:
        model = Game
        fields = ('id', 'game_type', 'title', 'make', 'gamer', 'number_of_players', 'skill_level')
