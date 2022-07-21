from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import Hospital, Staff, BaseUser
from .models import Hospital, Staff
from .models import BaseUser
from .forms import CustomUserCreationForm



class CustomUserAdmin(UserAdmin):
    """
    class for custom user admin to user look in admin
    """
    model = BaseUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User role',
            {
                'fields': (
                    'is_doctor',
                    'is_patient',
                )
            }
        )
    )

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Staff)
admin.site.register(BaseUser, CustomUserAdmin)
