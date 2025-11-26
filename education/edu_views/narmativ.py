from django.shortcuts import render

from education.edu_models.narmativ import Normative


def normative_list(request):
    normatives = Normative.objects.all()
    context = {
        'normatives': normatives,
    }
    return render(request, 'education/narmativ.html', context)