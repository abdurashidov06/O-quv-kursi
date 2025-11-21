from django.forms import forms

from education.edu_models.course import Course


class CourseForm(forms.Form):
    class Meta:
        model = Course
        fields = [
            'name',
            'image',
            'description',
            'duration',
            'price',
        ]
