from django.urls import path
from . import views

urlpatterns = [
    path('api/getRandomNumber', views.get_random_number),
    
]
