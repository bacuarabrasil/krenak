from ..environment import env


SWAGGER_SETTINGS = {
    "DEFAULT_API_URL": env.str("KRENAK_API_BASE_API_URL", default="https://example.com"),
}
