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
        # pyuwsgi.run("--strict", "--need-app", "--module", "wsgi", )
        # del sys.argv[0]
        # import subprocess

        print(sys.argv)
        pyuwsgi.run()

        # subprocess.run(["uwsgi", *sys.argv[1:]])

        # subprocess.run(
        # ["uwsgi"] + sys.argv + ["--strict", "--need-app", "--module", "wsgi"]
        # )


if __name__ == "__main__":
    main()
