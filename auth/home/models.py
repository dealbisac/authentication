from django.db import models

# Create your models here.
class Student(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=100)
    anonymousname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
