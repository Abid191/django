from django.urls import path 
from . import views

urlpatterns = [
    path('fc/',views.free_courses),
    path('blog/',views.blog),
]