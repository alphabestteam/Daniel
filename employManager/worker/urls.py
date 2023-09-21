# workers/urls.py
from django.urls import path
from worker.views import update_delete_worker, worker

urlpatterns = [
    path('workers/', worker, name='worker-list'),
    path('delete_update_worker/<int:id>/', update_delete_worker, name='delete_update_worker'),
]
