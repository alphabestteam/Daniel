from django.db import models

class People(models.Model):

    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField()
    person_id = models.IntegerField(primary_key= True)
    city = models.TextField()    

