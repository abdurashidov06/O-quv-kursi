from django.shortcuts import render

from education.edu_models.teacher import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    context={
        'teachers':teachers,
    }
    return render(request, 'education/teacher.html', context)