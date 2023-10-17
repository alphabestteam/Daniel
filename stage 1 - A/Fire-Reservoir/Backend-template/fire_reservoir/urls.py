from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("targets.urls"))
    # Add here the targets URL
]
