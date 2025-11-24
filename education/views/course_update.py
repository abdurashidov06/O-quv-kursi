from django.shortcuts import redirect, render

from education.edu_models.course import Course
from education.forms.course import CourseForm


# update

# def course_update(request):
#     course = Course.objects.get(id=request.POST.get('course_id'))
#     if request.method == 'POST':
#         form = CourseForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/course')
#         else:
#             form = CourseForm(instance=course)
#             context = {
#                 'form': form,
#             }
#             return render(request, 'courses-update.html', context)



# def update_course(request,pk):
#     course = Course.objects.filter(pk=pk).first()
#     if request.method == 'POST':
#         form = CourseForm(request.POST,instance=course)
#         if form.is_valid():
#             form.save()
#             return redirect("course:list")
#     else:
#         form = CourseForm(instance=course)
#     context = {
#         'form': form
#     }
#     return render(request, "course/form.html", context)