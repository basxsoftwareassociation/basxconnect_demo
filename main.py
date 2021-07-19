import os
import sys

import pyuwsgi


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "basxconnect_demo.settings.production"
    )

    if "manage" in sys.argv[1:2]:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv[1:])
    else:
        pyuwsgi.run("--strict", "--need-app", "--module", "wsgi", *sys.argv[1:])


if __name__ == "__main__":
    main()
