from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def english(request):
    return render(request,'courses/english.html')

def bangla (request):
    return render(request,'courses/bangla.html')

def math (request):
    return render(request,'courses/math.html')

def biology (request):
    return render(request,'courses/biology.html')
