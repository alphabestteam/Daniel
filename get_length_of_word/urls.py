from django.urls import path
from . import views

urlpatterns = [

    path('api/getLengthOfWord/<str:word>', views.get_length_of_word),
]
