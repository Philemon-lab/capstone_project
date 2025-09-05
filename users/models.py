from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('passenger', 'passenger'),
        ('agency', 'agency'),
        ('admin', 'admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='passenger')
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
