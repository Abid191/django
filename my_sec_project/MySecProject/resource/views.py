from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    course1 = '2 bangla course'
    course2 = '5 math course'
    course3 = 'english course 8'
    course4 = '4 biology course' 

    allCourses = {"c1": course1,"c2": course2,"c3": course3,"c4": course4}

    return render(request,"resources/blog.html",allCourses)

def free_course(request):
    return render(request, "resources/freeCourse.html", {'fcrs':5})
