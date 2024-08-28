import os
import environ
from pathlib import Path

from django.templatetags.static import static
from django.utils.translation import gettext_lazy as _


env = environ.Env(DEBUG=(bool, False))

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(os.path.join(BASE_DIR, "settings/.env"))

SECRET_KEY = env("SECRET_KEY")

DEBUG = env("DEBUG", default=True, cast=bool)

VERSION = "0.1.0"

ENVIRONMENT = env("ENVIRONMENT", default="development")

PROJECT_NAME = env("PROJECT_NAME", default="PROJECT NAME")

ALLOWED_HOSTS = []

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

EXTERNAL_APPS = [
    "rest_framework",
    "debug_toolbar",
    "rosetta",

    # Swagger
    "drf_yasg",

    # Unfold
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
]

PROJECT_APPS = [
    "apps.core",
]

INSTALLED_APPS = PROJECT_APPS + EXTERNAL_APPS + DJANGO_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages"
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

LANGUAGES = [
    ('pt-br', 'PT-BR'),
    ('en', 'EN'),
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Recife"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "core.Account"

# Swagger

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Basic': {
            'type': 'basic'
        }
    }
}

SWAGGER_OPENAPI_TERM_OF_SERVICE = env(
    "SWAGGER_OPENAPI_TERM_OF_SERVICE",
    default="Insert term"
)

SWAGGER_OPENAPI_CONTACT = env(
    "SWAGGER_OPENAPI_CONTACT",
    default="Insert contact"
)

SWAGGER_OPENAPI_LICENSE = env(
    "SWAGGER_OPENAPI_LICENSE",
    default="Insert license"
)

# Unfold
UNFOLD = {
    "SITE_TITLE": env("PROJECT_NAME", default="Django Boilerplate"),
    "SITE_HEADER": env("PROJECT_NAME", default="Django Boilerplate"),
    "SITE_SYMBOL": "settings",  # Material Symbols & Icons
    "SHOW_HISTORY": True,
    "ENVIRONMENT": "apps.core.utils.environment_callback",
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
    },
    "LOGIN": {
        "image": lambda request: static("core/assets/admin/login-bg.jpg"),
    },
    "COLORS": {
        "primary": {
            "50": "232 236 255",
            "100": "208 218 255",
            "200": "174 190 255",
            "300": "125 152 255",
            "400": "84 121 255",
            "500": "68 102 255",
            "600": "58 89 229",
            "700": "49 76 204",
            "800": "42 65 178",
            "900": "35 54 151",
            "950": "18 28 102"
        }
    },
}

# Debug Toolbar config
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG}
