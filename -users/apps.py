import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "konnaxion.users"  
    verbose_name = "Users"
    label = "users"  
    
    def ready(self):
        with contextlib.suppress(ImportError):
            import konnaxion_project.users.signals  # noqa: F401
