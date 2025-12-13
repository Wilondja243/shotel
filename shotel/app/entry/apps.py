from django.apps import AppConfig


class ReportsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shotel.app.entry'

    def ready(self):
        import shotel.app.entry.signals
