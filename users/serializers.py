from rest_framework import serializers
from django.contrib.auth.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile information"""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id', 'username', 'email', 'first_name', 'last_name']
