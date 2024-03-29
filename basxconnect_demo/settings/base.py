# flake8: noqa
"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
import sys

from basxbread.settings.required import *

# the above will import a set of predefined settings to ensure required
# settings are defined correctly and to reduce verbosity in this file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "l+#35mz2=81hcda7z)$+_4!e^azx40mo83d-s1%0bc4e2jwo@2"

ALLOWED_HOSTS = []

# BASXBREAD_DEPENDENCIES are imported in the start import at the top
INSTALLED_APPS = (
    [
        "basxconnect.invoicing",
        "basxconnect.projects",
        "basxconnect.core",
        "django.contrib.admin",
        "basxbread.contrib.reports",
        "basxbread.contrib.publicurls",
        "basxbread.contrib.document_templates",
        "basxbread.contrib.customforms",
        "basxbread.contrib.triggers",
    ]
    + BASXBREAD_DEPENDENCIES
    + ["demoapp.apps.DemoAppConfig"]
)
TEMPLATES[0]["OPTIONS"]["context_processors"].append(
    "basxconnect.core.context_processors.basxconnect_core"
)


ROOT_URLCONF = "basxconnect_demo.urls"

WSGI_APPLICATION = "wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.join(BASE_DIR, "woosh_index"),
    },
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

COUNTRIES_FIRST = ["ch", "de", "fr", "uk"]

BASXCONNECT = {
    "PREFERRED_LANGUAGES": (
        "de",
        "fr",
        "en",
    ),
    "PREFERRED_CURRENCIES": ("CHF", "EUR"),
}
