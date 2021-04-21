# import pytest

# from krenak_api.apps.enrollments.models import Enrollment


# @pytest.mark.django_db
# def test_core_queryset_active(enrollment):
#     assert Enrollment.objects.count() == 0

#     active_user = enrollment(is_active=True)
#     enrollment(is_active=False)
#     enrollment(is_active=False)

#     assert Enrollment.objects.count() == 3
#     assert Enrollment.objects.active().count() == 1
#     assert Enrollment.objects.active().first() == active_user
