import os
import sys


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "basxconnect_demo.settings.production"
    )

    if "manage" in sys.argv[1:2]:
        from django.core.management import execute_from_command_line

        execute_from_command_line(sys.argv[1:])
    else:
        import pyuwsgi

        args = ["--module", "uwsgi"]
        if "--ini" in sys.argv:
            pos = sys.argv.index("--ini")
            args.extend(sys.argv[pos : pos + 2])

        print("**********************", args, "*******************")
        pyuwsgi.run(["--strict", "--nned-app", "--module", "wsgi"])


if __name__ == "__main__":
    main()
