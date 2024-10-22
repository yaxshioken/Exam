

from django.db import models
from django.utils.translation import gettext_lazy as _

from account.models import User


class StaffLogin(models.Model):
    staff = models.ForeignKey(
        User,
        verbose_name=_("Staff"),
        on_delete=models.CASCADE,
        related_name='user_stafflogin',
        limit_choices_to={'is_staff': True},
    )

    session_key = models.CharField(
        max_length=40,
        verbose_name=_("Session Key"),
    )
