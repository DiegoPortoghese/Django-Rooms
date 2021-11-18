from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    cap = models.CharField(max_length=10, blank=True, null=True)
    province = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    newsletter_consent = models.BooleanField(default=False)
    privacy_consent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username