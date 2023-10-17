from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=100)  
    attack_priority = models.IntegerField()  
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  
    enemy_organization = models.CharField(max_length=100)  
    target_goal = models.CharField(max_length=100)  
    was_target_destroyed = models.BooleanField()  
    target_id = models.IntegerField()  

    def __str__(self):
        return self.name  

