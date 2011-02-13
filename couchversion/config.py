from django.conf import settings

APP_VERSION = getattr(settings, "APP_VERSION", "0.0.0")
