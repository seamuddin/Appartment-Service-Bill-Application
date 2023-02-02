from django.db import models
from .validators import *
# Create your models here



class Member(models.Model):
    name = models.CharField(max_length=5, validators=[validate_even])
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    parmanent_address = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)

    # def save(self, force_insert=False, force_update=False):
    #     if len(self.name) > 5:
    #         raise ValidationError('Name must be greater than 4 character')
    #     # this can, of course, be made more generic
    #     models.Model.save(self, force_insert, force_update)


