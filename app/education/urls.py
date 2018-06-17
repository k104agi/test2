from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.student, name='student'),
    path('school/', views.school, name='school'),
    path('school/list', views.school_list, name='school_list'),
]