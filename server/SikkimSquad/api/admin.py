# your_app/admin.py

from django.contrib import admin
from .models import Monastery, LoginHistory # Import both models on one line

# --- Customizing the Monastery Admin Page ---
@admin.register(Monastery)
class MonasteryAdmin(admin.ModelAdmin):
    """
    This customizes how the list of monasteries is displayed.
    """
    list_display = ('name', 'latitude', 'longitude')
    search_fields = ('name', 'description')

# --- Customizing the LoginHistory Admin Page ---
@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    """
    This customizes the display for login records and makes them read-only.
    """
    list_display = ('user', 'login_timestamp', 'ip_address')
    list_filter = ('user', 'login_timestamp')
    search_fields = ('user__username', 'ip_address')
    
    # Since these records are created automatically, make them read-only in the admin
    readonly_fields = ('user', 'login_timestamp', 'ip_address', 'user_agent')

    # Optional: Prevent anyone from adding or deleting these records manually
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False