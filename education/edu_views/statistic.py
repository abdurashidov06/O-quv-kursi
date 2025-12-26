from django.shortcuts import render

from education.edu_models.course import Course
from education.edu_models.group import Group
from education.edu_models.student import Student
from education.edu_models.teacher import Teacher


def get_admin_page(request):
    course=Course.objects.count
    groups=Group.objects.count
    students=Student.objects.count
    teachers=Teacher.objects.count
    context={
        'course':course,
        'groups':groups,
        'students':students,
        'teachers':teachers,

    }
    return render(request, 'admin/landing.html', context)