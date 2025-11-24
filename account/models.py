# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from .acc_models import *
from django.db.models import ForeignKey


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student','Student'),
        ('teacher','Teacher'),
        ('admin','Admin')
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username

# class Student(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.PositiveIntegerField()
#     course = ForeignKey('Course', on_delete=models.CASCADE,related_name='students')
#     teacher = ForeignKey('Teacher', on_delete=models.CASCADE,related_name='students')
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# class Teacher(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.PositiveIntegerField()
#     course = ForeignKey('Course', on_delete=models.CASCADE,related_name='teachers')
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Admin(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     age = models.PositiveIntegerField()
#     course = ForeignKey('Course', on_delete=models.CASCADE,related_name='admins')
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"