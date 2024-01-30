from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Student(models.Model):
    email = models.EmailField()
    anonymousname = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    preapproval = models.BooleanField(default=False)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invite(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    preapproval = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

