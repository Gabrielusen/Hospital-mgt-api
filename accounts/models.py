from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.phonenumber import PhoneNumber


USER_CHOICE = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
]


class Hospital(models.Model):
    """ Class Hospital """
    hospital_name = models.CharField(max_length=255, default='')
    hospital_email = models.EmailField(max_length=255, default='')
    hospital_address = models.CharField(max_length=255, default='')
    hospital_phone_number = PhoneNumber()


    def __str__(self) -> str:
        return str(self.hospital_name)


class User(AbstractUser):
    """ Abstract class for users """
    user = models.ForeignKey(Hospital, on_delete=models.PROTECT, null=True, blank=True)
    roles = models.CharField(max_length=20, choices=USER_CHOICE, null=False, blank=False)


class Employees(models.Model):
    """ Class Table for Employees details"""
    hospital_name = models.ForeignKey(Hospital, on_delete=models.PROTECT, null=False, blank=True)
    first_name = models.CharField(max_length=50, default='', null=False, blank=True)
    last_name = models.CharField(max_length=50, default='', null=False, blank=True)
    middle_name = models.CharField(max_length=50, default='', null=False, blank=True)
    birth_date = models.DateField()
