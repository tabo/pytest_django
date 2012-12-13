from __future__ import absolute_import

from .settings_base import ROOT_URLCONF, INSTALLED_APPS, STATIC_URL, SECRET_KEY
from .settings_base import SITE_ID

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}
