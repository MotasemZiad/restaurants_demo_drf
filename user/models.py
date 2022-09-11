from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=5, primary_key=True)
    picture = models.URLField(max_length=255, null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # the User Django class contains name, is staff, and passwords fields

    def __str__(self):
        return self.user.username
