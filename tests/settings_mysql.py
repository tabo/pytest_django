from __future__ import absolute_import

from .settings_base import ROOT_URLCONF, INSTALLED_APPS, STATIC_URL, SECRET_KEY

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pytest_django',
        'HOST': 'localhost',
        'USER': 'root',
        'OPTIONS': {
            'init_command': 'SET storage_engine=InnoDB'
        }
    },
}
