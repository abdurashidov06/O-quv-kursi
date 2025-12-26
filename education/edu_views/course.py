from django.shortcuts import render, redirect

from education.edu_forms.course import CourseForm
from education.edu_models.course import Course


def get_courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course/course.html', context)


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    context = {
        'courses': course,
    }
    return render(request, 'course/detail.html', context)

def course_update(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.name=request.POST.get('name')
            form.description=request.POST.get('description')
            form.duration=request.POST.get('duration')
            form.price=request.POST.get('price')
            form.save()
            return render(request, 'course/detail.html', {})
    else:
        return render(request, 'course/update.html', {})

def course_delete(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.delete()
        return render(request, 'course/course.html')
    else:
        return render(request, 'course/delete.html')