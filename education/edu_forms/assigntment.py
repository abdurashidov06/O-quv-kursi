from django import forms

from education.edu_models.assignmentsubmission import AssignmentSubmission


class AssignMentForm(forms.ModelForm):
    class Meta:
        model=AssignmentSubmission
        fields=[
            'text',
            'file',

        ]


class CheckinAssignmentForm(forms.ModelForm):
    class Meta:
        model=AssignmentSubmission
        fields=[
            'grade',
            'comment',
        ]