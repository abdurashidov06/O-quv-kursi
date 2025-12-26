from django.urls import path
from education.edu_views.assign import checking_assign_list, mark_assign_student, create_assign, create_detail_normative
from education.edu_views.course import course_delete, course_detail, course_update, get_courses
from education.edu_views.group import get_group, group_detail, group_update, group_delete, add_student_group, \
    get_detail_group_student
from education.edu_views.narmativ import get_normative, create_normative
from education.edu_views.statistic import get_admin_page
from education.edu_views.student import get_student
from education.edu_views.teacher import get_teacher_page

# app_name = 'course'

urlpatterns=[

    # group
    path('',get_group,name='group-list'),
    path('<int:pk>/detail/', group_detail, name='group_detail'),
    path('<int:pk>/update/', group_update, name='group_update'),
    path('<int:pk>/delete/', group_delete, name='group_delete'),
    path("user-assign/<int:nor_pk>/", create_assign, name="user-create"),
    path("group/add/<int:pk>/", add_student_group, name="add-student-group"),
    path("group/detail-st/<int:pk>/", get_detail_group_student, name="add-student-group-detail"),
    # course
    path('course/<int:pk>', get_courses, name='course'),
    path('course/<int:pk>/detail', course_detail, name='course_detail'),
    path('course/<int:pk>/update', course_update, name='course_update'),
    path('course/<int:pk>/delete', course_delete, name='course_delete'),

    # normative
    path('normative/',get_normative,name='normative-list'),
    path('normative/create',create_normative,name='normative-create'),
    path("normative/detail/<int:pk>/",create_detail_normative,name="detail-normative"),

    # student
    path('student/',get_student,name='student-list'),

    # teacher
    # path('teacher/',get_teacher_page,name='teacher'),

#     statistic urls
    path("admin/landing/",get_admin_page,name="admin-landing"),
    path("teacher/new/",get_teacher_page,name="teacher-landing"),

    #assign
    path("assign/list/", checking_assign_list, name="assign-list"),
    path("assign/detail/<int:assign_pk>/", mark_assign_student, name="assign-detail")
]