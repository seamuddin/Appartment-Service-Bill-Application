from django.db import models

# Create your models here.
from tanent.models import Tanent


class BillHistory(models.Model):
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    tanent = models.ForeignKey(Tanent, on_delete=models.CASCADE)
    