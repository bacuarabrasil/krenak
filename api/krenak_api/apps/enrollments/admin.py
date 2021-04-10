from django import forms
from django.contrib import admin

from krenak_api.apps.enrollments.models import Enrollment, Interest


class EnrollmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        matches = self.instance.matches
        if "matches" in self.fields:
            w = self.fields["matches"].widget
            choices = []
            for choice in matches:
                choices.append((choice.id, choice.enrollee.email))
            w.choices = choices


class PartialEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = (
            "enrollee",
            "enrollment_type",
            "resume",
            "interests",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# Register your models here.
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    add_form = PartialEnrollmentForm
    form = EnrollmentForm
    list_display = (
        "enrollee",
        "enrollment_type",
        "enrollment_status",
    )
    search_fields = ("enrollee__email", "enrollment_type", "enrollment_status", "interests__description")
    ordering = ("enrollee",)
    readonly_fields = ["matches"]
    filter_horizontal = ["interests"]

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ("description",)
    search_fields = ("description",)
    ordering = ("description",)
