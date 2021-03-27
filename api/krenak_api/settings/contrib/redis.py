from ..environment import env


REDIS_URL = env.str("KRENAK_API_REDIS_URL", default="redis://redis:6379/2")
