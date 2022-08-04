from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    class serializer that turns python objects into JSON format
    """
    class Meta:
        """
        Meta class for serialization
        """
        model = User
        fields = '__all__'
