from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import School, Student


def index(request):
    return render(request, '.templates/education/index.html', {})


def student(request):
    return render(request, '.templates/education/student.html', {})


def school(request):
    return render(request, '.templates/education/school.html', {})


def school_list(request):
    school_list = School.objects.all()
    return render(request, 'templates/school_list.html', {'school_list': school_list})

# def school_detail(request):
#
# def student_list(request):
#
# def student_detail(request):
