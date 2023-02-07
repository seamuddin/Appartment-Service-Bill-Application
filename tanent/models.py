from django.db import models
from flat.models import *

# Create your models here.
import datetime
class Tanent(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    parmanent_address = models.CharField(max_length=100)
    nid = models.IntegerField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    datetime = models.CharField(max_length=10, default=None)