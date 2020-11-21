#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from io import StringIO
from dotenv import dotenv_values



def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DNA.settings')

    filelike = StringIO('SPAM=EGGS\n')
    filelike.seek(0)
    parsed = dotenv_values(stream=filelike)
    parsed['SPAM']

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
