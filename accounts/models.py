from django.db import models
from django.contrib.auth.models import AbstractUser


USER_CHOICE = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('R', 'Receptionist'),
    ('HR', 'HR')
]
# Create your models here.
class User(AbstractUser):
    """
    user class for different users in the database
    """
    user_type = models.CharField(choices=USER_CHOICE, max_length=3, default=None)

    def is_doctor(self):
        """ return True if the user is a doctor and False if not """
        if self.user_type == 'D':
            return True
        return False

    def is_patient(self):
        """ return True if the user is a patient and False if not """
        if self.user_type == 'P':
            return True
        return False

    def is_receptionist(self):
        """ return True if the user is a receptionist and False if not """
        if self.user_type == 'R':
            return True
        return False

    def is_hr(self):
        """ return True if the user is HR and False if not """
        if self.user_type == 'HR':
            return True
        return False

    class Meta:
        """ Descending order for id """
        # ordering = ('id',)
