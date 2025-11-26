from django.forms import forms

from education.edu_models.narmativ import Normative


class NormativeForm(forms.Form):
    class Meta:
        model = Normative
        fields = [
            'course',
            'mark',
            'title',
            'description',
            'file',
            'created_at',
            'teacher'
        ]