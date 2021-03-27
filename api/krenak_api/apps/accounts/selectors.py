from krenak_api.apps.accounts.models import UserAccount


def get_all_users():
    return UserAccount.objects.active()
