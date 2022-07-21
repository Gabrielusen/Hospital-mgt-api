from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import BaseUser


class CustomUserCreationForm(UserCreationForm):
    """
    class for custom creation form
    """
    class Meta:
        """
        meta class for custom creation forms
        """
        model = BaseUser
        fields = "__all__"
