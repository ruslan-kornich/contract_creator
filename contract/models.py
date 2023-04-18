import os

from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    short_name = models.CharField(max_length=200)
    code_company = models.CharField(unique=True, max_length=8)
    director = models.CharField(max_length=255)
    short_dir_name = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    bank_account = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255)
    mfo = models.CharField(max_length=255)
    date_generate = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.short_name} - code {self.code_company}"


def get_upload_path(instance, filename):
    return os.path.join("contracts", str(instance.user.id), filename)


class Template(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=get_upload_path)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="templates")

    def __str__(self):
        return f"{self.name}"


class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


class ContractFile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    file = models.FileField(upload_to="contracts/")
