from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from people.models import People
from people.serializers import PeopleSerializer
import json


@csrf_exempt
def add_person(request):
   if request.method == 'POST':
        object_data = JSONParser().parse(request)
        data_deserialized = PeopleSerializer(data=object_data)
        if data_deserialized.is_valid():
            data_deserialized.create(object_data)
            return HttpResponse("Added person successfully")
        else:
            return HttpResponse("cannot save person, the object is not in good format")
        
@csrf_exempt
def update_person(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        person_id = data['person_id']
        person = People.objects.get(person_id=person_id)
        person_serialized = PeopleSerializer(person,data=data)
        if person_serialized.is_valid():
            person_serialized.update(person,data)
            return HttpResponse({'update person successfully'})
        return HttpResponse("Failed to update.")


def get_all(request):
    if request.method == 'GET':
        people = People.objects.all() 
        people_serialized = PeopleSerializer(people, many=True)
        return JsonResponse(people_serialized.data, safe=False)
    
@csrf_exempt
def delete_person(request, id):
    if request.method == 'DELETE':
        try:
            person = People.objects.get(person_id=id)
            person.delete()
            return JsonResponse({'message': 'Person deleted successfully'}, status=200)
        except People.DoesNotExist:
            return JsonResponse({'error': 'Person not found.'}, status=404)
    