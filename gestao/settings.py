"""
Django settings for gestao project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

TOKEN_VERIFY = '123456789'

ACCESS_TOKEN = 'EAAkLjcwPZB64BAHZAM6yEW3tUSgLDuwnegv42TtuBMWtxEwRZBb9dM0Tf4ZCY4764LZCZCkpjIriZA4OjV3cFZAbHdDcMhyWtehTZAN98kPIKYwfGr88ftdZAtnCBe6uAUQ7mJCkBghbOolaMTQ69DgeUyvCkNWYjXeFbe3zxLNHWYxQZDZDz'
ACCESS_TOKEN2 = 'EAAlX1c8ZCs6QBAOGu9xBx85ryarriJzSdvo3TXsaqunvkjHmQAURZA55eeZCm8ViWNwhCAhOE0CfTZBG5khOvZBIRPF79trWlOJF4cRxHBgmVWvZCRBubWpMe3pIjWhNFrDtNl9uBwkUKw1Jj0kR3zZAFLa7apZCHWtIi6oXhRKdVZBZAerBGK8mH8'
ACCESS_TOKEN3 = 'EAAlX1c8ZCs6QBANUmQsNTaueeVZBFbIIU1RihI4gklZAgIXnFaiKPMTbGe08AZAg2SOhEazb2rBIwCJh9fXZBlsRv7u2ZAboOZBp0uZA3UA09Ayw3mV2Qx4Oyp9yRQLaI5L0kVZCBuwfHe4uAENFMNB860eru4IwqtmzCNGIVtlXRMwZDZD'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c7z37=a+yu!)-mu^@lr)dssd%p^q-jb@o5^r$u&vr51bzl=#27'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'comparador',
    'comparador.template_tags',
    'teste',
    'chatbot',
    'chatterbot.ext.django_chatterbot',
    'channels',
    'pousada',
    'cotacao'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'template_form': 'comparador.template_tags.template_form',

            }
        },
    },
]


CHATTERBOT = {
    'name': 'Tech Support Bot',
    'logic_adapters': [
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    'trainer': 'chatterbot.trainers.ChatterBotCorpusTrainer',
    'training_data': [
        'chatterbot.corpus.portuguese.greetings'
    ]
}

WSGI_APPLICATION = 'gestao.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

USE_L10N = True
USE_THOUSAND_SEPARATOR = True

DATE_FORMAT = "d-M-Y"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')

STATIC_URL = '/static/'

ASGI_APPLICATION = "gestao.routing.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
