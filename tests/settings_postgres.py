from __future__ import absolute_import

from .settings_base import ROOT_URLCONF, INSTALLED_APPS, STATIC_URL, SECRET_KEY

# PyPy compatibility
try:
    from psycopg2ct import compat
    compat.register()
except ImportError:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pytest_django',
        'HOST': 'localhost',
        'USER': '',
    },
}
