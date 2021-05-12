from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str("KRENAK_BASE_API_URL", default="https://example.com"),
    "SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}},
}
