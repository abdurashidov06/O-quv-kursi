from django.forms import forms

from education.edu_models.group import Group


class GroupForm(forms.Form):
    class Meta:
        model = Group
        fields = [
            'name',
            'course',
            'teacher',
            'students',
            'start_date',
            'end_date',
        ]