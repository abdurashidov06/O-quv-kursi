from django import forms

from education.edu_models.course import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'name',
            'image',
            'description',
            'duration',
            'price',
        ]

