"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Access configparser to load variable values
from django.utils.six.moves import configparser
config = configparser.SafeConfigParser(allow_no_value=True)
config.read(os.path.join(BASE_DIR, 'setup/preprod_setting.cfg'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config.get('security', 'SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get('general', 'DEBUG')

ALLOWED_HOSTS = config.get('general', 'ALLOWED_HOSTS').split(",")


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'public',
    'bootstrap3',
    'crispy_forms',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'mailchimp',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates/'),],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('databases', 'ENGINE'),
        'NAME': config.get('databases', 'NAME'),
        'USER': config.get('databases', 'USER'),
        'PASSWORD': config.get('databases', 'PASSWORD'),
        'HOST': config.get('databases', 'HOST'),
        'PORT': config.get('databases', 'PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR,"prodstatic")
MEDIA_ROOT = os.path.join(BASE_DIR,"prodmedia")
STATICFILES_DIRS = [
os.path.join(BASE_DIR,"static"),
os.path.join(BASE_DIR,"media"),
]

SITE_ID = 1

# CUSTOM : Crispforms Setup part
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# CUSTOM : Allauth Setup part
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    )

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False
SOCIALACCOUNT_QUERY_EMAIL = ACCOUNT_EMAIL_REQUIRED
#Since users don't have account on the landing page, sign up redirect to thank you page
LOGIN_REDIRECT_URL = '/thank-you'
#ACCOUNT_FORMS = {'signup': 'public.forms.MySignupForm'}

#GMAIL basic setup
EMAIL_BACKEND = config.get('mail', 'EMAIL_BACKEND')
DEFAULT_FROM_EMAIL = config.get('mail', 'DEFAULT_FROM_EMAIL')
EMAIL_HOST = config.get('mail', 'EMAIL_HOST')
EMAIL_HOST_USER = config.get('mail', 'EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config.get('mail', 'EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# CUSTOM : Django-Mailchimp Setup part
MAILCHIMP_API_KEY = config.get('security', 'MAILCHIMP_API_KEY')
MAILCHIMP_SUBSCRIBE_LIST_ID = config.get('security', 'MAILCHIMP_SUBSCRIBE_LIST_ID')
