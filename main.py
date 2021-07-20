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
        # for option in ["--module=wsgi"]:
        # if option.split("=") not in sys.argv:
        # sys.argv.append(option)
        # del sys.argv[0]
        print("**********************", sys.argv[1:], "*******************")
        pyuwsgi.run(sys.argv[1:])


if __name__ == "__main__":
    main()
