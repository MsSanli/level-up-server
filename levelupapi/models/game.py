from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):

    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE, related_name='game')
    title = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='game')
    number_of_players = models.IntegerField(default=1, null=True, blank=True)
    skill_level = models.IntegerField(default=0, null=True, blank=True)
    
    
# There will be 5 main tables, Gamer, Game, GameType, EventGamer and Event.
# Each of those tables have some fields that would be useful to keep track of in the database.
# The Game table will have a one to many relationship with GameType since a game will be associated with 1 game type and a game type can be associated with many games.
# The Game will also have a one to many relationship with Gamer because gamers can create more than one game.
# The Event table will have a one to many relationship with Gamer, called the organizer, because gamers can host many events but an event will only have 1 host.
# To keep track of who is attending events, there is a many to many relationship between gamers and events. There will need to be a join table to connect that many to many relationship. That's where the EventGamer table comes in.
