"""
Django settings for django_base project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os

from pathlib import Path

from decouple import Csv
from decouple import config
from dj_database_url import parse as dburl

from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

SITE_ID = 1

ADMINS = (
    ('DevOps', 'devops@serverbit.com.br'),
)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',
    'django.contrib.gis',
    'django_extensions',
    'django_base.apps.account.apps.AccountConfig',
    'django_base.apps.thumbnail.apps.ThumbnailConfig',
    'django_base.apps.website.apps.WebsiteConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'django_base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'django_base/apps/account/templates'),
            os.path.join(BASE_DIR, 'django_base/apps/website/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'django_base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DEFAULT_DBURL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': config('DATABASE_URL', default=DEFAULT_DBURL, cast=dburl),
}

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# The custom authentication backend used to support soft exclusion of accounts.
# AUTHENTICATION_BACKENDS = ['django_base.libs.auth.backends.ModelBackend']

AUTH_USER_MODEL = 'account.User'

LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587

SERVER_EMAIL = 'noreply@django_base.com.br'
DEFAULT_FROM_EMAIL = 'noreply@django_base.com.br'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('pt', _('Portuguese'))
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'django_base/apps/account/locale'),
    os.path.join(BASE_DIR, 'django_base/apps/website/locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_AWS_BUCKET = config('STATIC_AWS_BUCKET', default='')

DEFAULT_STATICFILES_STORAGE_VALUE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_STORAGE = config('STATICFILES_STORAGE', default=DEFAULT_STATICFILES_STORAGE_VALUE)

if STATICFILES_STORAGE == DEFAULT_STATICFILES_STORAGE_VALUE:
    STATIC_ROOT = os.path.join(BASE_DIR, 'django_base', 'static')


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'django_base/apps/website/static'),
)

MEDIA_URL = '/media/'

MEDIA_AWS_BUCKET = config('MEDIA_AWS_BUCKET', default='')

DEFAULT_FILE_STORAGE_VALUE = 'django.core.files.storage.FileSystemStorage'
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE', default=DEFAULT_FILE_STORAGE_VALUE)

# Defines an appropriate path to store media in case of default value in DEFAULT_FILE_STORAGE.
# usually this happens when in development.
if DEFAULT_FILE_STORAGE == DEFAULT_FILE_STORAGE_VALUE:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'django_base', 'media')


AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = 'public-read'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY', default='')

STATIC_CUSTOM_DOMAIN = config('STATIC_CUSTOM_DOMAIN', default='')
MEDIA_CUSTOM_DOMAIN = config('MEDIA_CUSTOM_DOMAIN', default='')