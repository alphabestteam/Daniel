from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
import json

from targets.models import Target
from targets.serializers import TargetSerializer

@csrf_exempt
def add_target(request):
    if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = TargetSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.create(object_data).save()
            return HttpResponse("The target was saved!")
        else:
            return HttpResponse("cannot save object, the object not in good format")

        
@csrf_exempt
def update_target(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        target_id = data['target_id']
        target = Target.objects.get(target_id=target_id)
        target_serialized = TargetSerializer(target,data=data)
        if target_serialized.is_valid():
            target_serialized.update(target,data).save()
            return HttpResponse({'update target successfully'},safe=False, status=status.HTTP_200_OK)
        return HttpResponse("Failed to update.", status=status.HTTP_400_bad_REQUEST)


def all_targets(request):
    targets = Target.objects.all()
    serializer = TargetSerializer(targets, many=True)
    return JsonResponse(serializer.data, safe=False)

