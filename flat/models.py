from django.db import models

# Create your models here.
from member.models import Member


class Flat(models.Model):
    flat_no = models.CharField(max_length=255)
    size = models.IntegerField()
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)
