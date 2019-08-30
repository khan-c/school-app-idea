from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from datetime import date
from .constants import TEACHER, PARENT, STUDENT


# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(default=0, validators=[
                              MinValueValidator(0)], blank=True)
    birthdate = models.DateField(default=date(1900, 1, 1), blank=True)
    teachers = models.ManyToManyField(
        "self", verbose_name="teachers", blank=True, related_name="teachers")
    parents = models.ManyToManyField(
        "self", verbose_name="parents", blank=True, related_name="parents")
    role_choices = [
        (TEACHER, 'Teacher'),
        (PARENT, 'Parent'),
        (STUDENT, 'Student'),
    ]
    role = models.CharField(
        max_length=1, choices=role_choices, default=STUDENT)
    profile_pic = models.ImageField(verbose_name="profile pic", blank=True)

    def __str__(self):
        return self.email
