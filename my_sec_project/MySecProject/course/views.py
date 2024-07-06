from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def english(request):
    return render(request,'english.html')

def bangla (request):
    return HttpResponse('welcome to Bangla Course')

def math (request):
    return HttpResponse('welcome to Math Course')

def biology (request):
    return HttpResponse('welcome to Biology Course')
