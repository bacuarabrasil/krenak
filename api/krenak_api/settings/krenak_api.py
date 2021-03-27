from datetime import timedelta

from .environment import env


KRENAK_API_FEATURES = env.list("KRENAK_API_FEATURES", default=[])

KRENAK_API_EMAIL_FROM = env.str("KRENAK_API_EMAIL_FROM", default="no-reply@example.com")

KRENAK_API_AUTH_COOKIE_NAME = env.str("KRENAK_API_AUTH_COOKIE_NAME", default="a")

# Reset password link lifetime interval (in seconds). By default: 1 hour.
KRENAK_API_RESET_PASSWORD_EXPIRATION_DELTA = timedelta(
    seconds=env.int("KRENAK_API_RESET_PASSWORD_EXPIRATION_DELTA", default=3600)
)

if "LOG_SQL" in KRENAK_API_FEATURES:  # pragma: no cover
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
        "formatters": {
            "simple": {"format": "[%(asctime)s] %(levelname)s %(message)s"},
            "verbose": {"format": "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"},
            "sql": {"()": "krenak_api.loggers.SQLFormatter", "format": "[%(duration).3f] %(statement)s"},
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "verbose", "level": "DEBUG"},
            "sql": {"class": "logging.StreamHandler", "formatter": "sql", "level": "DEBUG"},
        },
        "loggers": {
            "django.db.backends": {
                "handlers": ["sql"],
                "level": "DEBUG",
                "filters": ["require_debug_true"],
                "propagate": False,
            },
            "django.db.backends.schema": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        },
    }
