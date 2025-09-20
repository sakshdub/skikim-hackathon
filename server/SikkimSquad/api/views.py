from django.contrib.auth import authenticate
from django.contrib.auth.signals import user_logged_in
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework_simplejwt.tokens import RefreshToken

# --- Correct Imports ---
# Import all the necessary models and serializers
from .serializers import UserSerializer, MonasterySerializer, AccommodationBookingSerializer
from .models import Monastery, AccommodationBooking
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly 

# --- RegisterView (No changes) ---
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --- LoginView (No changes) ---
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            user_logged_in.send(sender=user.__class__, request=request, user=user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful!',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# --- LogoutView (No changes) ---
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# --- ProfileView (No changes) ---
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# --- MonasteryViewSet (No changes) ---
class MonasteryViewSet(viewsets.ModelViewSet):
    queryset = Monastery.objects.all()
    serializer_class = MonasterySerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# --- AccommodationBookingViewSet (This is the updated part) ---
class AccommodationBookingViewSet(viewsets.ModelViewSet):
    """
    This viewset handles creating and viewing bookings.
    """
    serializer_class = AccommodationBookingSerializer
    # Only authenticated users can interact with their bookings.
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        """
        This is a security feature: users can only see their OWN bookings,
        not bookings made by other people.
        """
        user = self.request.user
        return AccommodationBooking.objects.filter(owner=user)

    def perform_create(self, serializer):
        """
        This is the magic part: when a new booking is created,
        it automatically assigns the logged-in user as the owner.
        """
        serializer.save(owner=self.request.user)

