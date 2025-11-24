from django import models
from django.db.models import ForeignKey


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    course = ForeignKey('Course', on_delete=models.CASCADE,related_name='teachers')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"