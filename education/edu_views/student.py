from django.shortcuts import render

from education.edu_models.student import Student


def get_student(request):
    students = Student.objects.all().order_by('-id')
    student_data = []

    for student in students:
        total_grade = sum(a.grade if a.grade is not None else 0 for a in student.assign_student.all())
        student_data.append({
            'student': student,
            'total_grade': total_grade
        })

    context = {
        'student_data': student_data
    }

    return render(request, 'student/student_list.html', context)