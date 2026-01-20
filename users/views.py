from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer


class UserProfileView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve the authenticated user's profile information
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Return the currently authenticated user
        return self.request.user
