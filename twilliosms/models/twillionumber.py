from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from server.models import BaseModel
from .twilliosettings import TwillioSettings
from .twilliosms import TwillioSMS



class TwillioNumber(BaseModel):
    """
    """

    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=_("Number Owner"),
    )

    twillioSettings = models.ForeignKey(
        TwillioSettings,
        on_delete=models.CASCADE,
        verbose_name=_("Twillio Settings"),
    )

    number =  models.CharField(
        max_length=32, default=_("twillionumer"), verbose_name=_("Twillio number")
    )


    def sendSms(self):
        pass

    class Meta(BaseModel.Meta):
        verbose_name = _("Twillio number")
        verbose_name_plural = _("Twillio Numbers")
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.number
