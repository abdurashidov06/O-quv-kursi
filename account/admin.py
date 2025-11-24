from django.contrib import admin

from education.edu_models.course import Course
from education.edu_models.group import Group
from education.edu_models.narmativ import Normative
from education.edu_models.student import Student
from education.edu_models.teacher import Teacher

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Normative)
admin.site.register(Student)
admin.site.register(Teacher)
