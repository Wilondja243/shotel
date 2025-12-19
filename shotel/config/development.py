
from pathlib import Path

from .base import *


SECRET_KEY = "django-insecure-+&5lxnu(o0z(@!9al))z^-))fcmzfqm(^pgruuw4x!$26!j^67"
DEBUG = True

ALLOWED_HOSTS=['*']

# Cookie
CSRF_COOKIE_NAME="csrftoken"
CSRF_HEADER_NAME='HTTP_X_CSRFTOKEN'

# Email backend
EMAIL_BACKEND="django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="wilondjaebuela2001@gmail.com"
EMAIL_HOST_PASSWORD="eqal xqyf rfal zhry "
EMAIL_TIMEOUT=30


CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
]

try:
    from .local_settings import *
except ImportError:
    pass
