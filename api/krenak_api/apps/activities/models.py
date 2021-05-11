from django.db import models
from django.utils.translation import gettext_lazy as _
from krenak_api.apps.common.models import CoreModel
from krenak_api.apps.accounts.models.user_account import UserAccount
from krenak_api.apps.mentorships.models import Mentorship


class Activity(CoreModel, models.Model):
    title = models.CharField(verbose_name="Title", blank=True, max_length=30, null=True)
    description = models.TextField(verbose_name="Description", blank=True, max_length=500, null=True)
    mentorship = models.ForeignKey(Mentorship, verbose_name="Mentorship", on_delete=models.CASCADE, null=True,  related_name="activities")

class Task(CoreModel, models.Model):
    title = models.CharField(verbose_name="Title", blank=True, max_length=30, null=True)
    done = models.BooleanField(verbose_name="Done", blank=True, default=False, null=True)
    activity = models.ForeignKey(Activity, verbose_name="Activity", on_delete=models.CASCADE, null=False, related_name="tasks")

class Comment(CoreModel, models.Model):
    text = models.CharField(verbose_name="Text", blank=True, max_length=30, null=True)
    author =  models.ForeignKey(UserAccount, verbose_name="Author", on_delete=models.CASCADE, null=False)
    activity = models.ForeignKey(Activity, verbose_name="Activity", on_delete=models.CASCADE, null=True,  related_name="comments")
