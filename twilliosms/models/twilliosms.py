from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_str, smart_text
from django.conf import settings
from django.core import validators
import re

from twilio.rest import Client

from server.models import BaseModel




class TwillioSMS(BaseModel):
    """
        Validate number based on https://en.wikipedia.org/wiki/E.164
    """

    smsFrom = models.ForeignKey(
        "twilliosms.TwillioNumber",
        on_delete=models.PROTECT,
        default=1,
        related_name='messages',
        verbose_name=_("Twillio Number")
    )


    smsTo = models.CharField(
        max_length=256, default=_("Gateway Name"), verbose_name=_("Server name"),
        validators=[
        validators.RegexValidator(regex=re.compile('^\+[1-9]\d{1,14}$'),message=_("Please check the number"))
        ],
    )

    smsMessage = models.CharField(
        max_length=256, default=_("Gateway Name"), verbose_name=_("Server name")
    )


    class Meta(BaseModel.Meta):
        verbose_name = _("Twillio SMS ")
        verbose_name_plural = _("Twillio SMSs")
        indexes = [
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.smsTo
