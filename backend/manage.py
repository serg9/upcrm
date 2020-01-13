#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upcrm.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environmepython manage.py runservernt variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()