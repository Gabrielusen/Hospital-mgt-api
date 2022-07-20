from distutils.command.upload import upload
from email.policy import default
from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
#  from django.contrib.auth.models import User
#   import uuid
# Create your models here.


#class BaseUser(AbstractUser):
#
#    #Abstract user class for multi-user types for when one user can assume only one role,
#    central point to check the type of user

#    DOCTOR = 1
#    PATIENT = 2
#
#    ROLE_CHOICES = (
#        (1, 'Doctor'),
#        (2, 'Patient'),
#    )
#    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


class BaseUser(AbstractUser):
    """
    class model for if user on the application can assume multiple roles at the same time
    """
    is_doctor = models.BooleanField('doctor_status', default=False)
    is_patient = models.BooleanField('patient_status', default=False)
    is_admin = models.BooleanField('admin_status', default=False)


class Hospital(models.Model):
    """
    Hospital class that contains information of the hospital
    """
    # hospital_id = models.UUIDField(default='', unique=True, primary_key=True)
    hospital_user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, default='')
    hospital_name = models.CharField(max_length=255, blank=False, default='')
    hospital_address = models.CharField(max_length=100, blank=False, default='')
    hospital_phone = PhoneNumberField()
    hospital_email = models.EmailField(max_length=254, default='')


    def __str__(self):
        return str(self.hospital_name)

class Staff(models.Model):
    """
        model for staff information within the hospital
    """

    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    staff_first_name = models.CharField(max_length=100, blank=False, default='')
    staff_last_name = models.CharField(max_length=100, blank=False, default='')
    staff_middle_name = models.CharField(max_length=100, blank=False, default='')
    staff_gender = models.CharField(max_length=20, choices=gender, default='M')
    staff_dob = models.DateField(default=None, null=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE) 
    # staff_profile_pic = models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return self.staff_first_name + ' ' + self.staff_middle_name + ' ' + self.staff_last_name


#   class Department(models.Model):
