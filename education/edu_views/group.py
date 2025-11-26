from django.shortcuts import render

from education.edu_models.group import Group


def get_group(request):
    groups = Group.objects.all()
    context = {
        'groups': groups,
    }
    return render(request, 'education/group.html', context)