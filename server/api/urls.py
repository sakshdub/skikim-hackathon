# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileView, LogoutView, MonasteryViewSet

# --- Router for ViewSets ---
# The router automatically creates the URLs for the Monastery API
router = DefaultRouter()
router.register(r'monasteries', MonasteryViewSet, basename='monastery')

# --- Manual Paths for Standard Views ---
# These are your user-related pages
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
    
    # --- Include the router's URLs ---
    # This adds the generated /monasteries/ and /monasteries/<id>/ URLs
    path('', include(router.urls)),
]