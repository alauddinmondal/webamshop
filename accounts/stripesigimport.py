from django.apps import AppConfig

class StripeAppconfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from . import signals