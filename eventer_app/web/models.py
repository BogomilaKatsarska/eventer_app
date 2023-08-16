from django.core.validators import MinValueValidator
from django.db import models

from eventer_app.web.validators import validate_date_not_in_the_past, validate_sting_contains_only_letters


class Profile(models.Model):
    MAX_LEN_FIRST_NAME = 20
    MIN_LEN_LAST_NAME = 4
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_EMAIL = 45
    MIN_LEN_PASSWORD = 5
    MAX_LEN_PASSWORD = 20

    first_name = models.CharField(
        max_length=20,
        validators=(
            validate_sting_contains_only_letters,
        ),
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            MinValueValidator(MIN_LEN_LAST_NAME),
        ),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=MAX_LEN_EMAIL,
        null=False,
        blank=False,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    password = models.CharField(
        max_length=MAX_LEN_PASSWORD,
        validators=(
            MinValueValidator(MIN_LEN_PASSWORD),
        ),
        null=False,
        blank=False,
    )


class Event(models.Model):
    MIN_LEN_EVENT_NAME = 2
    MAX_LEN_EVENT_NAME = 30
    MAX_LEN_CATEGORY = 14

    SPORTS = 'Sports'
    FESTIVALS = 'Festivals'
    CONFERENCES = 'Conferences'
    PERFORMING_ART = 'Performing Art'
    CONCERTS = 'Concerts'
    THEME_PARTY = 'Theme Party'
    OTHER = 'Other'

    CATEGORIES = (
        (SPORTS, SPORTS),
        (FESTIVALS, FESTIVALS),
        (CONFERENCES, CONFERENCES),
        (PERFORMING_ART, PERFORMING_ART),
        (CONCERTS, CONCERTS),
        (THEME_PARTY, THEME_PARTY),
        (OTHER, OTHER),
    )

    event_name = models.CharField(
        max_length=MAX_LEN_EVENT_NAME,
        validators=(
            MinValueValidator(MIN_LEN_EVENT_NAME),
        ),
        null=False,
        blank=False,
    )
    category = models.CharField(
        max_length=MAX_LEN_CATEGORY,
        choices=CATEGORIES,
        null=False,
        blank=False,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date = models.DateField(
        validators=(
            validate_date_not_in_the_past,
        ),
        null=False,
        blank=False,
    )
    event_image = models.URLField(
        null=False,
        blank=False,
    )
