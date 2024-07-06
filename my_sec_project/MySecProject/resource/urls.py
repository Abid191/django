from django.urls import path 
from . import views 

urlpatterns = [
    path('blog/',views.blog),
    path('fc/',views.free_course),
]