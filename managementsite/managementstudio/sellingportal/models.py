from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=150)
    Email = models.CharField(max_length=150)
    Phone = models.IntegerField(max_length=20)
    age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    comment = models.CharField(max_length=100)

class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)
class Meta:
    model = User
    Fields = ['username', 'email', 'password']