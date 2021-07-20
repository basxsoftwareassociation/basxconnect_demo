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
        import configparser

        import pyuwsgi

        args = []
        if "--ini" in sys.argv:
            config = configparser.ConfigParser()
            config.read(sys.argv[sys.argv.index("--ini") + 1])
            for key, value in config["uwsgi"].items():
                if key != "privileged-binary-patch":
                    args.append(f"--{key}")
                    args.append(value)

        defaultargs = ["--strict", "--need-app", "--module", "wsgi"]

        print("**********************", *(args + defaultargs), "*******************")
        pyuwsgi.run(*(args + defaultargs))


if __name__ == "__main__":
    main()
