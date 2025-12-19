import dj_database_url
from pathlib import Path
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(',')

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://shotel-n6id.onrender.com",
    "http://127.0.0.1:3000",
]

# Database
DATABASES = {
    'default': dj_database_url.config(default=config("DATABASE_URL"), ssl_require=True)
}

# Email
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast = int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_TIMEOUT = config('EMAIL_TIMEOUT', cast = int)

# Cookie
CSRF_COOKIE_NAME = config('CSRF_COOKIE_NAME')
CSRF_HEADER_NAME = config('CSRF_HEADER_NAME')

CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE")
CSRF_COOKIE_HTTPONLY = config("CSRF_COOKIE_HTTPONLY")

SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE")

SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT")
SECURE_PROXY_SSL_HEADER = config("SECURE_PROXY_SSL_HEADER").split(',')
SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT")
SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS", cast = int)
SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD")
SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS")


