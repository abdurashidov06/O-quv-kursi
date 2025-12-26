from django.shortcuts import redirect, render

from education.edu_forms.narmative import NormativeForm
from education.edu_models.narmativ import Normative


def create_normative(request):
    if request.method=='POST':
        form=NormativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form=NormativeForm()
    return render(request,"normative/form.html",{'form':form})


def get_normative(request):
    normatives=Normative.objects.all()
    return render(request,"normative/normative.html",{'normatives':normatives})