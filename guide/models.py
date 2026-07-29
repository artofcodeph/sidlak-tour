from django.core.checks import model_checks
from django.db import models

# Create your models here.
class Guide(models.Model):
    full_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    area = models.CharField(max_length=100)
    specialization = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name
