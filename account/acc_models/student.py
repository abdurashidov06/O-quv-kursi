from django.db.models import ForeignKey

from django import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    course = ForeignKey('Course', on_delete=models.CASCADE ,related_name='students')
    teacher = ForeignKey('Teacher', on_delete=models.CASCADE ,related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"