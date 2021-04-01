# flake8: noqa
"""
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from bread.settings.required import *

# the above will import a set of predefined settings to ensure required
# settings are defined correctly and to reduce verbosity in this file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "l+#35mz2=81hcda7z)$+_4!e^azx40mo83d-s1%0bc4e2jwo@2"

ALLOWED_HOSTS = []

# BREAD_DEPENDENCIES are imported in the start import at the top
INSTALLED_APPS = (
  [
    "django.contrib.admin",
    # "customization.apps.CustomizationConfig",  # custom config should be the first entry in the list
    "basxconnect.core.apps.CoreConfig",
  ]
    + BREAD_DEPENDENCIES
    + ["demoapp.apps.DemoAppConfig"]  # this needs to be at the end if we override layouts in the bread layout registry
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

BRANDING = {
    "platform": "basxConnect",
    "company": "Demo",
}
