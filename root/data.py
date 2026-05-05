from django.db import models
from django.utils.translation import gettext_lazy as _


class registration(models.TextChoices):
    CHECK_NIN = 'check_nin', _('Check NIN')
    VERIFIED = 'verified', _('Verified')
    FAILED = 'failed', _('Failed')

class genre(models.TextChoices):
    NULL   = '', _('Select/ اختر')
    m   = 'm', _('Male/ ذكر')
    f      = 'f', _('Female/ أنثى')

   