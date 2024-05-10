#!/usr/bin/env python
import os
import sys
if __name__ == '__main__':
    if "test" in sys.argv:
        raise Exception(
            '\nWe don\'t support Python UnitTest module here. Please run "pytest" command for running the unit tests.'
            '\nYou can look at the features it provide at https://pytest-django.readthedocs.io/en/latest/'
        )
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_based_QnA_with_ChatGPT.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
