"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from levelupapi.models import Event, Game, Gamer
from levelupapi.models.event_gamer import EventGamer


class EventView(ViewSet):
    """Level up events view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event 
        Returns:
            Response -- JSON serialized event 
        """
        event_view = Event.objects.get(pk=pk)
        serializer = EventSerializer(event_view)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        event_view = Event.objects.all()
        serializer = EventSerializer(event_view, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(uid=request.data["organizer"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            game=game,
            organizer=gamer,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
            Response -- Empty body with 204 status code
        """

        event = Event.objects.get(pk=pk)
        event.description = request.data["description"]
        event.date = request.data["date"]
        event.time = request.data["time"]

        # Update the game
        game = Game.objects.get(pk=request.data["game"])
        event.game = game

        # Update the organizer
        gamer = Gamer.objects.get(pk=request.data["organizer"])
        event.organizer = gamer

        # Save the updated event to the database
        event.save()

        # Return a 204 No Content response to indicate success
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    # @action(methods=['post'], detail=True)
    # def signup(self, request, pk):
    #     """Post request for a user to sign up for an event"""

    #     gamer = Gamer.objects.get(user=request.data["userId"])
    #     event = Event.objects.get(pk=pk)
    #     attendee = EventGamer.objects.create(
    #         gamer=gamer,
    #         event=event
    #     )
    #     return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['post'], detail=True)
    def signup(self, request, pk):
        """Post request for a user to sign up for an event"""

        try:
            gamer = Gamer.objects.get(uid=request.data["uid"])  # Use 'uid' instead of 'userId'
            event = Event.objects.get(pk=pk)
            attendee = EventGamer.objects.create(
                gamer=gamer,
                event=event
            )
            return Response({'message': 'Gamer added'}, status=status.HTTP_201_CREATED)
        except Gamer.DoesNotExist:
            return Response({'error': 'Gamer not found'}, status=status.HTTP_404_NOT_FOUND)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        fields = ('id', 'game', 'description', 'date', 'time', 'organizer')
