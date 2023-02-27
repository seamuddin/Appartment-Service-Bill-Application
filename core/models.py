from django.db import models

# Create your models here.
class CustomPermission(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name