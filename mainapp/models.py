from django.db import models
# Create your models here.
from tanent.models import Tanent
from django.utils.timezone import now

class BillHistory(models.Model):
    month = models.CharField(max_length=2)
    year = models.CharField(max_length=4)
    tanent = models.ForeignKey(Tanent, on_delete=models.CASCADE)
    amount = models.FloatField()
    status = models.IntegerField()
    invoice_number = models.CharField(max_length=20, default='0')
    date = models.DateTimeField(default=now())
    