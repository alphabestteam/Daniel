from django.db import models

class People(models.Model):

    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    person_id = models.IntegerField(primary_key= True)
    city = models.TextField()    
class Parent(People):
    job = models.CharField(max_length=255) 
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    kids = models.ManyToManyField(People, related_name='parents',default=[]) 
