from django.urls import path
from . import views

urlpatterns = [
    path('',views.english),
    path('ban/',views.bangla),
    path('ma/',views.math),
    path('bio/',views.biology)
]
