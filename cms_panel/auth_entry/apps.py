from django.apps import AppConfig


class AuthEntryConfig(AppConfig):
    name = 'auth_entry'


# from django.apps import AppConfig
# from django.utils.translation import ugettext_lazy as _
#
#
# class CMSConfig(AppConfig):
#     name = 'auth_entry'
#     verbose_name = _("django AUTH_ENTRY")
#
#     def ready(self):
#         from cms.utils.setup import setup
#
#         setup()
