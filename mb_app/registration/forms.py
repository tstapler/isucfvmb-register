from django import forms
from django.forms import extras
from django.core.validators import RegexValidator
from registration.choices import *
from registration.models import Student


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    first_name = forms.CharField(
        label="First Name",
        max_length=200
    )

    last_name = forms.CharField(
        label="Last Name",
        max_length=200
    )

    gender = forms.ChoiceField(
        choices=GENDERS,
        initial='Male'
    )

    student_id = forms.CharField(
        label="Student ID Number",
        max_length=9)

    ensemble = forms.ChoiceField(
        choices=ENSEMBLES
    )

    netid = forms.CharField(
        label="ISU Net-ID (netid@iastate.edu)",
        max_length=200
    )

    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    phone_number = forms.CharField(
        label="Cellphone Number",
        validators=[phone_regex],
        max_length=15
    )
    # validators should be a list
    medical_conditions = forms.CharField(
        label="Medical Conditions",
        widget=forms.Textarea
    )

    dietary_needs = forms.ChoiceField(
        label="Dietary Needs",
        choices=MEALS
    )

    hometown = forms.CharField(
        max_length=300
    )

    instrument = forms.ChoiceField(
        choices=INSTRUMENTS
    )

    movein_date = forms.DateField(
        label="Move In Date",
        widget=extras.SelectDateWidget()
    )

    years_tenure = forms.ChoiceField(
        label="Years in the Band",
        choices=YEARS
    )

    senior_ceremonies = forms.BooleanField(
        label="Are you participating in the senior ceremonies?",
        required=False
    )

    shoe_size = forms.ChoiceField(
        label="Shoe Size",
        choices=SHOE_SIZES
    )

    tshirt_size = forms.ChoiceField(
        label="T-Shirt Size",
        choices=TSHIRT_SIZES
    )

    parent_name = forms.CharField(
        label="Parent Name",
        max_length=100
    )

    parent_address = forms.CharField(
        label="Parent Address",
        max_length=300
    )

    parent_email = forms.EmailField(
        label="Parent Email"
    )

