"""
Django settings for DNA project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECRET_KEY = '_37@a5jgf3g)5+n4*5lg-0j8jr_sb7+w707u#0hy&o)oclh=jd'
SECRET_KEY = config('SECRETKEY')
DEBUG = config("DEBUG")

ALLOWED_HOSTS = ['https://dnappserver.herokuapp.com/', '127.0.0.1']




AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

INSTALLED_APPS = [
'django.contrib.contenttypes',
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.sites',
'django.contrib.staticfiles',
'rest_framework',
'rest_framework.authtoken',
'rest_auth',
'allauth',
'allauth.account',
'rest_auth.registration',
'allauth.socialaccount',
'allauth.socialaccount.providers.facebook',
'allauth.socialaccount.providers.google',
'api',
]


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '329679158218337',
            'secret': 'f63d610c89c1317fdea68c13ebf493ce',
            'key': ''
        }
    }
}


SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000", "",
]

ROOT_URLCONF = 'DNA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DNA.wsgi.application'
EMAIL_BACKEND = config('EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_TLS = config('EMAIL_USE_TLS')


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



if DEBUG == True:  #Use SQlite locally
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
else: #Use Postgress in Production
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbhcserc6q8n5g',
        'HOST': 'ec2-34-224-229-81.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'txhgvqikfbeubt',
        'PASSWORD':'03740e38ebc415692ab48c8c41bc2eae79c70c510a8f818ddeb0032607b5013e'
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

MEDIA_ROOT = os.path.join(BASE_DIR, 'profile')
MEDIA_URL = '/profile/'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



django_heroku.settings(locals())
