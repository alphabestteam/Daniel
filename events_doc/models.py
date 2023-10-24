from django.db import models
from users.models import User

class Event(models.Model):
    STATUS_CHOICES = [
    ('Closed', 'Closed'),
    ('Open', 'Open'),
    ('Waiting for Response', 'Waiting for Response'),
    ('Waiting for Handling', 'Waiting for Handling'),
] 
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, default="unknown")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_draft = models.BooleanField(default=True)
    is_archived = models.BooleanField(default=False)
    
