from django.urls import path
from . import views  

urlpatterns = [

    path('GetAll', views.get_all, name='get_all'),
    path('GetAllParents', views.get_all_parents, name='get_all_parents'),
    path('AddPerson', views.add_person, name='add_person'),
    path('UpdatePerson', views.update_person, name='update_person'),
    path('UpdateParent', views.update_parent, name='update_parent'),
    path('DeletePerson/<int:id>', views.delete_person, name='delete_person'),
    path('linkChildToParent', views.link_child_to_parent, name='link_child_to_parent'),
    path('AddParents', views.add_parents, name='add_parents'),
    path('parent/<int:parent_id>', views.get_parent_and_children, name='get_parent_and_children'),
    path('richKids', views.rich_kids, name='rich_kids'),
    path('findParents/<int:child_id>', views.find_parents, name='find_parents'),
    path('findChild/<int:parent_id>', views.find_children, name='find_children'),
    path('findGrandparents/<int:grandchild_id>', views.find_grandparents, name='find_grandparents'),
    path('findSibling/<int:child_id>', views.find_siblings, name='find_siblings')

]