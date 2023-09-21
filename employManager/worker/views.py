from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Worker
from worker.serializer import WorkerSerializer


@api_view(['GET', 'POST'])
def worker(request):
    if request.method == 'GET':
        workers = Worker.objects.all()
        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE', 'PUT'])
def update_delete_worker(request, id):
    try:
        worker = Worker.objects.get(id=id)
    except Worker.DoesNotExist:
        return Response('User not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        worker.delete()
        return Response('User deleted successfully!', status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        return Response('PUT request logic goes here', status=status.HTTP_200_OK)