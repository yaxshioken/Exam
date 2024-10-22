from django.contrib.auth.models import AbstractUser
from django.db import models

from account.choices import Status, RoleChoices

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    role = models.CharField(max_length=120,choices=RoleChoices.choices)

    def __str__(self):
        return self.username





class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    assignes = models.ManyToManyField(User, related_name='project_assignes')

    def __str__(self):
        return self.name


class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=Status.choices)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    assignes = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name


class TaskUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
