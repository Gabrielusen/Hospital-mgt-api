from rest_framework import generics
from .serializers import UserSerializer
from accounts.models import User


class UserApiView(generics.ListAPIView):
    """
    class for view apis
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
