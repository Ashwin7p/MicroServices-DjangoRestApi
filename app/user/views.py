"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions # rest_framework gives us base classes to override basic model operations like create with custom

from user.serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)

class CreateUserView(generics.CreateAPIView): #CreateAPIView, http requests to create objects in database
    """Create a new user in the system."""
    serializer_class = UserSerializer #url -> view -> serializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication] #Authentication to use for this view
    permission_classes = [permissions.IsAuthenticated] # permissions required to access only authenticated

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user