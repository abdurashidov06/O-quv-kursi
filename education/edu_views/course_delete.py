# from django.shortcuts import redirect, render
#
# from education.edu_models.course import Course
#
#
# # def course_delete(request):
# #     course_id = request.GET.get('course_id')
# #     course = Course.objects.get(id=course_id)
# #     course.delete()
# #     return redirect('course')
#
# def delete_course(request,pk):
#     course = Course.objects.filter(pk=pk).first()
#     if request.method == 'POST':
#         course.delete()
#         return redirect('course:list')
#     else:
#         return render(request, "course/delete.html", {'course':course})