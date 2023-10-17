from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.person_id = validated_data.get('person_id', instance.person_id)
        instance.city = validated_data.get('city', instance.city)

        instance.save()

        return instance