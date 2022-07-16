from distutils.command.upload import upload
from pickle import FALSE
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class Hospital(models.Model):
    """
    Hospital class that contains information of the hospital
    """
    hospital_user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=255, blank=False)
    hospital_address = models.CharField(max_length=100, blank=False)
    hospital_phone = PhoneNumberField()
    hospital_email = models.EmailField(max_length=254)


    def __str__(self):
        """
        return field object as string representation
        """
        return self.hospital_name

class Staff(models.Model):
    """
        model for staff information within the hospital
    """

    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    staff_first_name = models.CharField(max_length=100, blank=False)
    staff_last_name = models.CharField(max_length=100, blank=False)
    staff_middle_name = models.CharField(max_length=100, blank=False)
    staff_gender = models.CharField(max_length=20, choices=gender, default='M')
    staff_birthday = models.DateField(default=None, null=False)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    # staff_profile_pic = models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return self.staff_first_name + ' ' + self.staff_middle_name + ' ' + self.staff_last_name