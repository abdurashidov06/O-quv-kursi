from django.shortcuts import render

from education.edu_models.student import Student


def get_student(request):
    student = Student.objects.all()
    context = {
        'student': student,
    }
    return render(request, 'education/student.html', context)