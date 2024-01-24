from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField()
    anonymousname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
