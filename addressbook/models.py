from datetime import datetime
from django.db import models

# Create your models here.

class Models(models.Model):
    name = models.CharField(max_length=40, unique=True)
    email = models.CharField(max_length=60, unique=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = "Models"

