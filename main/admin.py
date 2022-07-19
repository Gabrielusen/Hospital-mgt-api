from django.contrib import admin
from .models import Hospital, Staff, User

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Staff)
admin.site.register(User)
