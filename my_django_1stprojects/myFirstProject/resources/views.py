from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def free_courses(request):
    return render(request,'freecources.html',{'fcrs':5})

def blog(request):
    return render(request,'blog.html')
