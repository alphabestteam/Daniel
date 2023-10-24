from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import User
from users.serializer import UserSerializer



@api_view(['POST'])
def add_User(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET'])
def users_list(request):
    users_list = User.objects.all()
    serializer = UserSerializer(users_list, many=True)
    return Response(serializer.data)