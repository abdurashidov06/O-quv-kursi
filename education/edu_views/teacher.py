from django.shortcuts import render

from education.edu_models.group import Group
from permissions.teacher import teacher_requered


# @teacher_requered
def get_teacher_page(request):
    # user=request.user
    # groups=Group.objects.filter(teacher=user.id).count()
    # admin=Group.objects.filter(teacher=user.id).all()
    # students=[student.students.count() for student in admin]
    # context={
    #     'groups':groups,
    #     'students':students[0]
    # }
    return render(request,'teacher/teacher_landing.html')