from django.db import models
from django.utils.translation import gettext_lazy as _

from krenak_api.apps.accounts.models.user_account import UserAccount
from krenak_api.apps.common.models import CoreModel


class Interest(CoreModel, models.Model):
    description = models.CharField(verbose_name="Description", blank=True, max_length=30, null=True)

    def __str__(self):
        return str(self.description)


class Enrollment(CoreModel, models.Model):
    class EnrollmentType(models.TextChoices):
        MENTOR = "MTR", _("Mentor")
        MENTEE = "MTE", _("Mentee")

    class EnrollmentStatus(models.TextChoices):
        SENT = "SE", _("Sent")
        AWAITING = "AW", _("Awaiting")
        ONGOING = "ON", _("Ongoing")
        FINISHED = "FI", _("Finished")

    resume = models.TextField(verbose_name="Resume", blank=True, max_length=500, null=True)
    enrollee = models.ForeignKey(UserAccount, verbose_name="Enrolle account", on_delete=models.CASCADE, related_name="enrollments")
    enrollment_type = models.CharField(
        verbose_name="Enrollment type", max_length=3, choices=EnrollmentType.choices, default=EnrollmentType.MENTEE
    )
    enrollment_status = models.CharField(
        verbose_name="Enrollment status", max_length=2, choices=EnrollmentStatus.choices, default=EnrollmentStatus.SENT
    )
    interests = models.ManyToManyField(Interest)

    @property
    def matches(self):
        try:
            matches = (
                Enrollment.objects.exclude(enrollment_type__contains=self.enrollment_type)
                .filter(interests__in=self.interests.all())
                .distinct()
                .filter()
            )
        except Enrollment.DoesNotExist:
            matches = None
        return matches

    def __str__(self):
        return str(f"<{self.enrollment_type} - {self.id}> {self.enrollee.get_full_name()}")
