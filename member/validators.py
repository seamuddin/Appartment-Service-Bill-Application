from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if len(value) > 5:
        raise ValidationError(
            _('%(value)s will not more than 5 character'),
            params={'value': value},
        )