from pickle import FALSE
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=255, blank=False)
    hospital_address = models.CharField(max_length=100, blank=False)
    hospital_phone = PhoneNumberField()
    hospital_email = models.EmailField(max_length=254)

    def __str__(self):
        return self.hospital_name

class Staff(models.Model):

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
    staff_profile_pic = models.ImageField()


 