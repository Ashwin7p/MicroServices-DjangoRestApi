"""
Views for the user API.
"""
from rest_framework import generics # rest_framework gives us base classes to override basic model operations like create with custom

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView): #CreateAPIView, http requests to create objects in database
    """Create a new user in the system."""
    serializer_class = UserSerializer #url -> view -> serializer