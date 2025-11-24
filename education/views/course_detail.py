from django.shortcuts import render

from education.edu_models.course import Course

# def course_detail(request, pk):
#     course = Course.objects.filter(pk=pk).first()
#     context = {
#         'c': course
#     }
#     return render(request, "course/detail.html", context)