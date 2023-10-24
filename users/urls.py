from django.urls import path
from . import views  

urlpatterns = [
    path('addUser', views.add_User, name='add_person'),
    path('allUsers', views.users_list, name='users_list'),
]