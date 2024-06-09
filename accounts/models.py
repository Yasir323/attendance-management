from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    )
    DEPARTMENT_CHOICES = (
        ('engineering', 'Engineering'),
        ('accounts', 'Accounts'),
        ('sales', 'Sales'),
        ('operations', 'Operations'),
    )
    role = models.CharField(max_length=16, choices=ROLE_CHOICES)
    age = models.IntegerField()
    department = models.CharField(max_length=16, choices=DEPARTMENT_CHOICES)
