# Generated by Django 4.0.6 on 2022-07-16 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_alter_staff_staff_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_profile_pic',
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='hospital_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
