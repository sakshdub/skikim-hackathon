# api/signals.py

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .models import LoginHistory

# This function is the "receiver" that listens for the signal
@receiver(user_logged_in)
def record_login_history(sender, request, user, **kwargs):
    """
    When a user logs in, create a LoginHistory record for them.
    """
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    LoginHistory.objects.create(
        user=user, 
        ip_address=ip_address,
        user_agent=user_agent
    )

    print(f"Login signal received for user: {user.username}") # For testing