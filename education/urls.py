from django.urls import path

from education.edu_models.course import Course
from education.views.group import get_group
from education.views.course import course_list
from education.views.narmativ import normative_list
from education.views.student import get_student
from education.views.teacher import get_teachers

urlpatterns=[
    path('course/',course_list,name='course'),
    path('group/',get_group,name='group'),
    path('narmativ/',normative_list,name='narmativ'),
    path('student/',get_student,name='student'),
    path('teacher/',get_teachers,name='teacher'),
]