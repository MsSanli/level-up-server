from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
  
  game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='event')
  description = models.CharField(max_length=50)
  date = models.DateField(blank=True)
  time = models.TimeField(blank=True)
  organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name='event')
  
  # game and organizer are foreign keys
  
# There will be 5 main tables, Gamer, Game, GameType, EventGamer and Event.
# Each of those tables have some fields that would be useful to keep track of in the database.
# The Game table will have a one to many relationship with GameType since a game will be associated with 1 game type and a game type can be associated with many games.
# The Game will also have a one to many relationship with Gamer because gamers can create more than one game.
# The Event table will have a one to many relationship with Gamer, called the organizer, because gamers can host many events but an event will only have 1 host.
# To keep track of who is attending events, there is a many to many relationship between gamers and events. There will need to be a join table to connect that many to many relationship. That's where the EventGamer table comes in.
