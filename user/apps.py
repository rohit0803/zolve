from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    def ready(self):
        import user.listeners	# pylint: disable=import-outside-toplevel, unused-import
        super().ready()
