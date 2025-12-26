import json

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from education.edu_models.assignmentsubmission import AssignmentSubmission
from education.edu_models.group import Group
from education.edu_models.student import Student


def get_group(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'group/group.html', context)


def group_detail(request):
    group=Group.objects.get(id=request.GET.get('id'))
    students = Student.objects.filter(group=group)
    context = {
        'group': group,
        'students': students,
    }
    return render(request, 'group/detail.html', context)

def group_delete(request):
    group=Group.objects.get(id=request.GET.get('id'))
    if request.method == 'POST':
        group.delete()
        return render(request, 'group/group.html')
    else:
        return render(request, 'group/delete.html')

def group_update(request):
    group=Group.objects.get(id=request.GET.get('id'))
    if request.method == 'POST':
        group.name=request.POST.get('name')
        group.teacher=request.POST.get('teacher')
        group.end_date=request.POST.get('end_date')
        group.save()
        return render(request, 'group/group.html')
    else:
        return render(request, 'group/update.html')


@login_required
@require_POST
def add_student_group(request, pk):
    try:
        data=json.loads(request.body)
        data_list=data.get("student_ids",[])
        group = Group.objects.get(pk=pk)

        with transaction.atomic():
            student = Student.objects.filter(pk__in=data_list)
            group.students.add(*student)
            group.save()
            return JsonResponse({"status": "success", "added": student.count()})
    except Exception as e:
        return JsonResponse({"status": "error", "error": str(e)}, status=500)


def get_detail_group_student(request, pk):
    group = Group.objects.get(pk=pk)
    students = group.students.all()
    assign=AssignmentSubmission.objects.filter(student__in=[obj.pk for obj in students])
    return render(request, 'group/group_detail_student.html', {"group":group,"students":students})