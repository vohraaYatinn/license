import uuid
from django.db import models

# Create your models here.
class LicenseKey(models.Model):
    license = models.TextField(primary_key=True)
    device = models.TextField(blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    registered = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.license}'
