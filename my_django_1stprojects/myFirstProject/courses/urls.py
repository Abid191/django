from django.urls import path 
from . import views


urlpatterns = [   
    path('',views.course ),
    path('ds/',views.data_science),
    path('bg/',views.big_data),
    path('fun/',views.fundamental),
    path('py/',views.python),
    path('eng/',views.english),
    path('ma/',views.math),
]