from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TwilliosmsConfig(AppConfig):
    name = "twilliosms"
    verbose_name = _("Twilliosms")

    def ready(self):
        import twilliosms.signals
