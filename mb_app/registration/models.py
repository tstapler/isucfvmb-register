from __future__ import unicode_literals
from django.core.validators import RegexValidator
from django.db import models
from swampdragon.models import SelfPublishModel
from registration.serializers import StudentSerializer
from registration.choices import *


# Create your models here.
class Student (SelfPublishModel, models.Model):
    serializer_class = StudentSerializer

    submission_time = models.DateTimeField(auto_now_add=True)

    first_name = models.CharField(
        max_length=200
    )

    last_name = models.CharField(
        max_length=200
    )

    student_id = models.CharField(
        max_length=9,
        unique=True
    )

    ensemble = models.CharField(
        max_length=9, choices=ENSEMBLES
    )

    netid = models.CharField(
        max_length=200
    )

    instrument = models.CharField(
        max_length=30, choices=INSTRUMENTS
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        blank=True,
        max_length=15
    )
    # validators should be a list
    hometown = models.CharField(
        max_length=300
    )

    movein_date = models.DateField()

    medical_conditions = models.TextField()

    dietary_needs = models.CharField(
        max_length=20,
        choices=MEALS
    )

    years_tenure = models.CharField(
        max_length=3,
        choices=YEARS
    )

    senior_ceremonies = models.BooleanField()

    gender = models.CharField(
        max_length=6,
        choices=GENDERS
    )

    shoe_size = models.CharField(
        max_length=6,
        choices=SHOE_SIZES
    )

    tshirt_size = models.CharField(
        max_length=6,
        choices=TSHIRT_SIZES
    )

    parent_name = models.CharField(
        max_length=100
    )

    parent_address = models.CharField(
        max_length=300
    )

    parent_email = models.EmailField()
