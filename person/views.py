import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from person.models import Parent, People
from person.serializers import ParentSerializer, PeopleSerializer
import json


@csrf_exempt
def add_person(request):
   if request.method == 'POST':
        try:
            object_data = JSONParser().parse(request)
            data_deserialized = PeopleSerializer(data=object_data)
            if data_deserialized.is_valid():
                data_deserialized.create(object_data)
                return HttpResponse("Added person successfully")
            else:
                return HttpResponse("Cannot save person, the object is not in the correct format", status=400)
        except:
            return HttpResponse(f"Failed to add  new person", status=500)

@csrf_exempt
def update_person(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            person_id = data['person_id']
            person = People.objects.get(person_id=person_id)
            person_serialized = PeopleSerializer(person, data=data)
            if person_serialized.is_valid():
                person_serialized.save()
                return HttpResponse("Update person successfully")
            else:
                return HttpResponse("Cannot update person, the object is not in the correct format", status=400)
        except People.DoesNotExist:
            return HttpResponse("Person not found.", status=404)

@csrf_exempt
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
@csrf_exempt
def get_all_parents(request):
    if request.method == 'GET':
        people = Parent.objects.all() 
        parents_serialized = ParentSerializer(people, many=True)
        return JsonResponse(parents_serialized.data, safe=False)  
     
@csrf_exempt
def add_parents(request):
    if request.method == 'POST':
        try:
            object_data = JSONParser().parse(request)
            data_deserialized = ParentSerializer(data=object_data)
            if data_deserialized.is_valid():
                data_deserialized.save()
                return HttpResponse("Added parents successfully")
            else:
                return HttpResponse("Cannot save parents, the object is not in the correct format", status=400)
        except:
            return HttpResponse(f"Failed to add parents", status=500)

@csrf_exempt    
def update_parent(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            person_id = data['person_id']
            person = Parent.objects.get(person_id=person_id)
            parent_serialized = ParentSerializer(person, data=data)
            if parent_serialized.is_valid():
                parent_serialized.save()
                return HttpResponse("Update parent successfully")
            else:
                return HttpResponse("Cannot update parent, the object is not in the correct format", status=400)
        except Parent.DoesNotExist:
            return HttpResponse("Parent not found.", status=404)
        except Exception as e:
            return HttpResponse(f"Failed to update parent", status=500)

    
@csrf_exempt
def link_child_to_parent(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            parent_id = data.get('parent_id')
            child_id = data.get('child_id')
            parent = Parent.objects.get(person_id=parent_id)
            child = People.objects.get(person_id=child_id)
            parent.kids.add(child)

            return JsonResponse({'message': 'Child linked to parent successfully'}, status=200)
        except (KeyError, Parent.DoesNotExist, People.DoesNotExist):
            return JsonResponse({'error': 'Invalid parent or child IDs.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

@csrf_exempt
def get_parent_and_children(request, parent_id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(person_id=parent_id)
            parent_serializer = ParentSerializer(parent)  
            children = parent.kids.all()
            children_serializer = PeopleSerializer(children, many=True)
    
            response_data = {
                'parent': parent_serializer.data,
                'children': children_serializer.data,
            }
            return JsonResponse(response_data, safe=False)
        except Parent.DoesNotExist:
            return JsonResponse({'error': 'Parent not found.'}, status=404)

@csrf_exempt
def rich_kids(request):
    if request.method == 'GET':
        try:
            rich_parents = Parent.objects.filter(salary__gt=50000.00)
            rich_kids = People.objects.filter(parents__in=rich_parents)
            rich_kids_list = []

            today = datetime.date.today()
            year = today.year

            for child in rich_kids:
                birth_year = child.date_of_birth.year
                age = year - birth_year
                if age < 18:
                    rich_kids_list.append(child)

            rich_kids_serializer = PeopleSerializer(rich_kids_list, many=True)

            return JsonResponse(rich_kids_serializer.data, safe=False)
        except Parent.DoesNotExist:
            return JsonResponse({'error': 'No rich parents found.'}, status=404)



@csrf_exempt
def find_parents(request, child_id):
    if request.method == 'GET':
        try:
            child = People.objects.get(person_id=child_id)
            parents = child.parents.all()
            parent_serializer = ParentSerializer(parents, many=True).data

            return JsonResponse(parent_serializer, safe=False)
        except People.DoesNotExist:
            return JsonResponse({'error': 'Person not found.'}, status=404)

@csrf_exempt
def find_children(request, parent_id):
    if request.method == 'GET':
        try:
            parent = Parent.objects.get(person_id=parent_id)
            children = parent.kids.all()
            children_serializer = PeopleSerializer(children, many=True)
            child_data = children_serializer.data

            return JsonResponse(child_data, safe=False)
        except Parent.DoesNotExist:
            return JsonResponse({'error': 'Parent not found.'}, status=404)
        

@csrf_exempt
def find_grandparents(request, grandchild_id):
    if request.method == 'GET':
        try:
            grandchild = People.objects.get(person_id=grandchild_id)
            parents = grandchild.parents.all()
            grandparents = []
            for parent in parents: 
                grandparents.extend(parent.parents.all())

            grandparents_serializer = ParentSerializer(grandparents, many=True).data

            return JsonResponse(grandparents_serializer, safe=False)
        except People.DoesNotExist:
            return JsonResponse({'error': 'Person not found.'}, status=404)
  

@csrf_exempt
def find_siblings(request, child_id):
    if request.method == 'GET':  
        try:
            child = People.objects.get(person_id=child_id)
            parents = child.parents.all()
            siblings = []

            for parent in parents:
                siblings.extend(parent.kids.all())

            sibling_serializer = PeopleSerializer(siblings, many=True)
            sibling_data = sibling_serializer.data

            return JsonResponse(sibling_data, safe=False)
        except People.DoesNotExist:
            return JsonResponse({'error': 'Child not found.'}, status=404)
