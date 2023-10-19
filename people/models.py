from django.core.validators import MaxValueValidator
from django.db import models


class People(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    person_id = models.IntegerField(primary_key=True)
    city = models.TextField()

class Parent(People):
    job = models.CharField(max_length=255)
    salary = models.IntegerField(
        validators=[MaxValueValidator(limit_value=999999)]
    )
    kids = models.ManyToManyField(People, related_name='parents',default=[])

    def __str__(self):
        return self.name
