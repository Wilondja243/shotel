from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shotel.app.user'

    def ready(self):
        import shotel.app.user.signals
