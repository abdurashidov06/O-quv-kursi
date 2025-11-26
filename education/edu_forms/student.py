from django.forms import forms

from education.edu_models.student import Student


class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = [
            'user',
            'avatar',
            'full_name',
            'email',
            'phone',
            'birth_date',
            'registered_at',
            'courses',
        ]