from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # --- ADD THIS PRINT STATEMENT ---
        print("✅ SUCCESS: ApiConfig ready() method is running. Attempting to import signals.")
        import api.signals

