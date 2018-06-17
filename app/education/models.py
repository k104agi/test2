from django.db import models
from django.utils import timezone


class School(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)


class Student(models.Model):
    def __str__(self):
        return self.name

    school = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(
        blank=True, null=True)

