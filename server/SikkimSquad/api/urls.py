# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# --- UPDATE THE IMPORT ---
# Import the new AccommodationBookingViewSet
from .views import RegisterView, LoginView, ProfileView, LogoutView, MonasteryViewSet, AccommodationBookingViewSet
from rest_framework_simplejwt.views import TokenRefreshView

# --- Router for ViewSets ---
router = DefaultRouter()
router.register(r'monasteries', MonasteryViewSet, basename='monastery')
# --- ADD THIS NEW LINE ---
# This creates the /bookings/ endpoint for your new API
router.register(r'bookings', AccommodationBookingViewSet, basename='booking')


# --- Manual Paths for Standard Views ---
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # --- Include the router's URLs ---
    path('', include(router.urls)),
]

