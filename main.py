import os
import sys

import django
import pyuwsgi


def main():
    # setup django
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "basxconnect_demo.settings.production"
    )

    if "manage" in sys.argv[1:2]:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv[1:])
    else:
        django.setup()
        from django.conf import settings

        pyuwsgi.run(*sys.argv[1:], *settings.PYUWSGI_ARGS)


if __name__ == "__main__":
    main()
