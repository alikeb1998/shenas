from django.apps import AppConfig


class ShenasappConfig(AppConfig):
    name = 'shenasapp'

    def ready(self):
        import shenasapp.signals
