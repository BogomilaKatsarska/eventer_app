from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_sting_contains_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('The name should contain only letters !')


def validate_date_not_in_the_past(value):
    if value < timezone.now().date():
        raise ValidationError("The date cannot be in the past!")


#TODO: fix validator and check above validator
def validate_contains_one_digit_or_more(value):
    for ch in value:
        pass
