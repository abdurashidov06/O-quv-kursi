from django.urls import path
from education.edu_views.course import course_delete, course_detail, course_update
from education.edu_views.group import get_group
from education.edu_views.course import course_list
from education.edu_views.narmativ import normative_list
from education.edu_views.student import get_student
from education.edu_views.teacher import get_teachers

app_name = 'course'

urlpatterns=[
    path('',course_list,name='course'),
    path('<int:pk>/detail/', course_detail, name='detail'),
    path('<int:pk>/update/', course_update, name='update'),
    path('<int:pk>/delete/', course_delete, name='delete'),
    path('group/',get_group,name='group'),
    path('narmativ/',normative_list,name='narmativ'),
    path('student/',get_student,name='student'),
    path('teacher/',get_teachers,name='teacher'),
]