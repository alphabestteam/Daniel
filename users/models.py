from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=225)
    user_name = models.CharField(max_length=225)
    person_id = models.IntegerField(primary_key= True)
    email = models.EmailField()
    # unread_messages = 
    