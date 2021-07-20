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

        args = []
        if "--ini" in sys.argv:
            pos = sys.argv.index("--ini")
            args.append(sys.argv[pos : pos + 2])

        print("**********************", args, "*******************")
        pyuwsgi.run(args)


if __name__ == "__main__":
    main()
