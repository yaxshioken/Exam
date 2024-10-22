from django.db.models import TextChoices


class Status(TextChoices):
    START='start','START'
    PROCESSING='processing','PROCESSING'
    FINISHED='finished','FINISHED'
    FAILED='failed','FAILED'
class RoleChoices(TextChoices):
    MAINTAINER='maintainer','MAINTAINER'
    DEVELOPER='developer','DEVELOPER'
