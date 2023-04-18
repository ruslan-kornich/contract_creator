from django.contrib.auth.models import User
from django.db import models
from contract.models import Template


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
