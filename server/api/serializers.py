# api/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Monastery

# --- UserSerializer (No changes) ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

# --- ADD THIS CLASS ---
# This is the serializer for your Monastery model
class MonasterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monastery
        fields = '__all__' # Includes all fields from your model