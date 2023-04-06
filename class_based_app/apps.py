from django.apps import AppConfig


class ClassBasedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'class_based_app'
