# coding: utf-8
"""
This module is used by the test runner.
"""
import os

print "settings de teste"

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

execfile(os.path.join(PROJECT_PATH, 'settings.py'))


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        'LOCATION': '',
    }
}

INSTALLED_APPS += (
    'api',
)

ALLOWED_HOSTS = ['*']