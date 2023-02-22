from django.db import models
from flat.models import *
from django.utils.timezone import now
# Create your models here.
import datetime
from .validators import validate_even
from django.core.exceptions import ValidationError

class Tanent(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    parmanent_address = models.CharField(max_length=100)
    nid = models.IntegerField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    date = models.DateField(default=now())
    end_date = models.DateField(default=None, null=True, blank=True)

    def clean(self):
        tanent = Tanent.objects.filter(flat_id = self.flat_id)
        if tanent:
            raise ValidationError({'Flat': 'This Flat Alrady Rent %s' % self.flat.flat_no})



class FlatChangeHistory(models.Model):
    tanent = models.ForeignKey(Tanent, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    date = models.DateField(default=now())
    status = models.IntegerField(default=0)


    def clean(self):
        if self.tanent and self.date:
            if self.tanent.end_date:
                if not self.tanent.date < self.date or not self.tanent.end_date < self.date:
                    raise ValidationError({'Rent Date': 'You are already living during this day %s' % self.date})
            else:
                if not self.tanent.date < self.date:
                    raise ValidationError({'Rent Date': 'You are already living during this day %s' % self.date})

