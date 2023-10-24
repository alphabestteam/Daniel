from rest_framework.decorators import api_view
from rest_framework.response import Response
from events_doc.models import Event
from events_doc.serializer import EventSerializer




@api_view(['POST'])
def add_event(request):
    data = request.data
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def events_list(request):
    events_list = Event.objects.all()
    serializer = EventSerializer(events_list, many=True)
    return Response(serializer.data)