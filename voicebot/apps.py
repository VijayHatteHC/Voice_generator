from django.apps import AppConfig


class VoicebotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'voicebot'
    def ready(self):
        from .utils import preload_models
        # Preload models once when the app is ready
        preload_models()
