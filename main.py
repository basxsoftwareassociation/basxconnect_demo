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

        args = ["--strict", "--need-app", "--module", "wsgi"]
        skipped_non_options = False
        for arg in sys.argv:
            skipped_non_options = skipped_non_options or arg.startswith("--")
            if skipped_non_options:
                args.append(arg)

        print("**********************", args, "*******************")
        pyuwsgi.run(*args)


if __name__ == "__main__":
    main()
