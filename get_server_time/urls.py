from django.urls import path
from . import views

urlpatterns = [
    path('api/currentTime', views.current_time),
    
]