from django.db.models import Q
from django.shortcuts import get_object_or_404

from account.models import User


def resolve_user(self, info, **kwargs):
        return User.objects.all()