#!/usr/bin/env python3
# via: http://stackoverflow.com/a/26637175/140800
import glob
import os
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))

# Unfortunately, apps can not be installed via ``modify_settings``
# decorator, because it would miss the database setup.
CUSTOM_INSTALLED_APPS = (
    'pennuser',
    'django.contrib.admin',
)

ALWAYS_INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

ALWAYS_MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


settings.configure(
    AUTH_USER_MODEL='pennuser.PennUser',
    AUTHENTICATION_BACKENDS=('pennuser.auth_backends.PennUserModelBackend',),
    SECRET_KEY="sWaVGkNXlHAcQNpQjVNOyVsJDQCcWG",
    DEBUG=False,
    TEMPLATE_DEBUG=False,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=ALWAYS_INSTALLED_APPS + CUSTOM_INSTALLED_APPS,
    MIDDLEWARE_CLASSES=ALWAYS_MIDDLEWARE_CLASSES,
    ROOT_URLCONF='tests.urls',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
        }
    },
    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,
    STATIC_URL='/static/',
    FIXTURE_DIRS=glob.glob(BASE_DIR + '/' + '*/fixtures/'),
)

django.setup()
args = [sys.argv[0], 'test']
# Current module (``tests``) and its submodules.
test_cases = '.'

# Allow accessing test options from the command line.
offset = 1
try:
    sys.argv[1]
except IndexError:
    pass
else:
    option = sys.argv[1].startswith('-')
    if not option:
        test_cases = sys.argv[1]
        offset = 2

args.append(test_cases)
# ``verbosity`` can be overwritten from command line.
args.append('--verbosity=2')
args.extend(sys.argv[offset:])

execute_from_command_line(args)
