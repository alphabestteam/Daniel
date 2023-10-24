from django.urls import path
from . import views  

urlpatterns = [
    path('addEvent', views.add_event, name='add_event'),
    path('allEvents', views.events_list, name='events_list'),
]