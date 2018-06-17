from django.shortcuts import render
from .models import *

def index(request):
    context = {
        'student': student,
    }
    return render(request, 'education/index.html', context)


def student(request, student_id):
    response = "You're looking at the results of student %s."
    return HttpResponse(response % student_id)


def school(request, school_id):
    response = "You're looking at the results of school %s."
    return HttpResponse(response % school_id)
