from django.shortcuts import render, redirect

from education.edu_models.course import Course
from education.edu_forms.course import CourseForm


def course_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'education/course.html', context)


def course_update(request):
    course = Course.objects.get(id=request.POST.get('course_id'))
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/course')
        else:
            form = CourseForm(instance=course)
            context = {
                'form': form,
            }
            return render(request, 'courses-update.html', context)


def course_detail(request, pk):
    course = Course.objects.filter(pk=pk).first()
    context = {
        'c': course
    }
    return render(request, "course/detail.html", context)


def course_delete(request,pk):
    course = Course.objects.filter(pk=pk).first()
    if request.method == 'POST':
        course.delete()
        return redirect('course:list')
    else:
        return render(request, "course/delete.html", {'course':course})