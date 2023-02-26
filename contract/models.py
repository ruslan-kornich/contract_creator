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
