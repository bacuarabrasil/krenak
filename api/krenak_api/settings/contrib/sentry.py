import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

from ..environment import env


USE_SENTRY = env.bool("KRENAK_API_USE_SENTRY", default=True)
if USE_SENTRY:  # pragma: no cover
    SENTRY_DSN = env.str("KRENAK_API_SENTRY_DSN")
    SENTRY_ENVIRONMENT = env.str("KRENAK_API_SENTRY_ENVIRONMENT")
    sentry_sdk.init(dsn=SENTRY_DSN, integrations=[DjangoIntegration()], environment=SENTRY_ENVIRONMENT)
