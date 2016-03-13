from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student (models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.CharField(max_length=9, min_length=9)
    ensemble = models.CharField(max_length=9)
    netid = models.charField(max_length=200)
    instrument = models.charField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)  # validators should be a list
    hometown = models.CharField(max_length=100)
    movein_date = models.DateField()
    medical_conditions = models.TextField()
    dietary_needs = models.CharField(max_length=20)
    years_tenure = models.CharField(max_length=3)
    senior_ceremonies = models.BooleanField()
