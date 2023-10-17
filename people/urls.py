from django.urls import path
from . import views  

urlpatterns = [

    path('GetAll', views.get_all, name='get_all'),
    path('AddPerson', views.add_person, name='add_person'),
    path('UpdatePerson', views.update_person, name='update_person'),
    path('DeletePerson/<int:id>', views.delete_person, name='delete_person')
   
]