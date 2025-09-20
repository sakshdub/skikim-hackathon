from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Monastery(models.Model):
    # This is the correct place for the owner field
    owner = models.ForeignKey(User, related_name='monasteries', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    main_image_url = models.URLField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
class LoginHistory(models.Model):
    
    # Link to the user who logged in
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # The exact time of the login
    login_timestamp = models.DateTimeField(auto_now_add=True)
    
    # The IP address of the user
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    
    # Information about the user's browser/device
    user_agent = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} logged in at {self.login_timestamp}'