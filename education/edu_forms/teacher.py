from django.forms import forms

from education.edu_models.teacher import Teacher


class TeacherForm(forms.Form):
    class Meta:
        model = Teacher
        fields=[
            'user',
            'full_name',
            'avatar',
            'phone',
            'specialization',
            'courses',
            'experience',
        ]