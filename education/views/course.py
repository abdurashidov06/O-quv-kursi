from django.shortcuts import render

from education.edu_models.course import Course


def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'education/course.html', context)
