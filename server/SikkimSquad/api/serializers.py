from django.contrib.auth.models import User
from rest_framework import serializers
# --- UPDATE THIS IMPORT ---
# Import all the models you need to serialize
from .models import Monastery, AccommodationBooking 

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

# --- MonasterySerializer (No changes) ---
class MonasterySerializer(serializers.ModelSerializer):
    # Add a field to show the owner's username, read-only
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Monastery
        fields = '__all__' # Includes all fields from your model

# --- ADD THIS NEW CLASS ---
# This is the serializer for your new AccommodationBooking model
class AccommodationBookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the AccommodationBooking model.
    The 'owner' is read-only because it's set automatically in the view 
    based on the logged-in user.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = AccommodationBooking
        # Include all fields from the model in the API response
        fields = '__all__'

