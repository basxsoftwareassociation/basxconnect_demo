from .base import *  # noqa

DEBUG = False
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

try:
    from .local import *  # noqa
except ImportError:
    pass

# this is used for easier settings configuration
# in prodcution environments
try:
    from instance_settings import *  # noqa
except ImportError as e:
    print(
        """You must have a file instance_settings.py somewhere in your python path.
The file must contain instance-specific django settings. It is recommended to set
at least the following settingg:

SECRET_KEY = "<random keys>"
ALLOWED_HOSTS = ["<domainname of instance>"]
ADMINS = [("Admin", "<admin-email-address>"), ]

"""
    )
