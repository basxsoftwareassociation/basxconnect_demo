import os
import sys

import pyuwsgi


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "basxconnect_demo.settings.production"
    )

    if "uwsgi" in sys.argv[1:2]:
        pyuwsgi.run(*sys.argv[2:], "--strict", "--need-app", "--module", "wsgi")
    else:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
