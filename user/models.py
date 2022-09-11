from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.


class Account(AbstractUser):
    username = None
    code = models.CharField(max_length=5, primary_key=True, unique=True)
    name = models.CharField(max_length=50, default="Pharmacy Name")
    picture = models.URLField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'code'
    objects = CustomUserManager()

    def __str__(self):
        return self.code
