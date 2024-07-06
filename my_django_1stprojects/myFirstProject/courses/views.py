from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. 

def course(request):
    return HttpResponse('welcome to our first project in django') 

def data_science(request):
    return HttpResponse('welcome to data_science') 

def big_data(request):
    return HttpResponse('welcome to bigData')

def fundamental(request):
    return HttpResponse('welcome to fundamental')

def python(request):
    return HttpResponse('welcome to python')

def english(request):
    return HttpResponse('welcome to english')

def math(request):
    return HttpResponse('welcome to math')
