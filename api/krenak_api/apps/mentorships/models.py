from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _

from krenak_api.apps.common import models as core_models
from krenak_api.apps.common.models import CoreModel
from krenak_api.apps.enrollments.models import Enrollment


def get_deadline():
    return datetime.today() + timedelta(days=20)


class Mentorship(CoreModel, models.Model):
    mentor_enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="given_mentorships")
    mentee_enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="received_mentorships")
    expiration_date = models.DateTimeField(default=get_deadline)

    def finish_mentorship(self):
        self.expiration_date = datetime.now()
        self.save()


class Goal(CoreModel, models.Model):
    mentorship = models.ForeignKey(Mentorship, null=False, blank=False, on_delete=models.CASCADE, related_name="goals")
    description = models.CharField(max_length=400, null=False, blank=False)
    accomplished_at = models.DateTimeField()
