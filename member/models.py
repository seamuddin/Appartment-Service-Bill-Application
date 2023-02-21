from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# Create your models here

# def validate_even(value):
#     if len(str(value)) > 5:
#         raise ValidationError(
#             _('%(value)s will not more than 5 character'),
#             params={'value': value},
#         )

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    parmanent_address = models.CharField(max_length=100)
    nid = models.IntegerField()

    # def save(self, force_insert=False, force_update=False):
    #     if len(self.name) > 5:
    #         raise ValidationError('Name must be greater than 4 character')
    #     # this can, of course, be made more generic
    #     models.Model.save(self, force_insert, force_update)


