from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
import base64
from server.models import BaseModel



class TwillioSettings(BaseModel):
    """"""

    accountSID = models.CharField(
        max_length=256, default=_("TwillioaccountSID"), verbose_name=_("account SID")
    )

    accountToken = models.CharField(
        max_length=256, default=_("accountToken"), verbose_name=_("account Token")
    )

    class Meta(BaseModel.Meta):
        verbose_name = _("Twillio Setting")
        verbose_name_plural = _("Twillio Settings")
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.accountSID
