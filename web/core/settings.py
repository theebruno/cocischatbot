"""
"""
import os
# import django_heroku

from decouple import config
from unipath import Path

# from django.core.urlresolvers import reverse_lazy

from django.shortcuts import redirect, reverse

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parent
CORE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'cocischatbott.herokuapp.com', config('SERVER', default='127.0.0.1')]
# ALLOWED_HOSTS = ['cocischatbott.herokuapp.com', ]

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'bootstrap_datepicker_plus',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    # 'rest_framework',
    'thumbnails',
    'whitenoise.runserver_nostatic',
    'widget_tweaks',
    'bootstrap4',

    # MY APPS
    'apps.accounts',
    'apps.profiles',
    'apps.home',
    # 'apps.courses',
    'apps.events',
    'apps.lecturer_offices',
    'apps.event_organisers',
    'apps.departments',
    'apps.course_units',
    'apps.class_timetables',
    'apps.exam_timetables',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

LOGIN_REDIRECT_URL = "home"  # Route defined in home/urls.py

LOGOUT_REDIRECT_URL = "home"  # Route defined in home/urls.py

TEMPLATE_DIR = os.path.join(CORE_DIR, "apps/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': 'db.sqlite3',

        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd948or6i1f4rsc',
        'USER': 'kovgnotaoxmglm',
        'PASSWORD': '386640934c45a6d57fbe6293b3a67defd8b88fe0cc65b0e8b44b4b71bd668365',
        'HOST': 'ec2-35-170-146-54.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

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

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(CORE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(CORE_DIR, 'apps/static'),
)

# heroku
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# EMAIL_HOST = 'smtp.email-host-provider-domain.com'
EMAIL_HOST = 'localhost'

# EMAIL_HOST_USER = 'yourusername@youremail.com'

# EMAIL_HOST_PASSWORD = 'your password'

EMAIL_PORT = 1025

# EMAIL_USE_TLS = True

# DEFAULT_FROM_EMAIL = 'theyuserteam@internet.com'

# ADMINS = (
#     ('You', 'you@email.com'),
# )

# MANAGERS = ADMINS

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'

from django.contrib import messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# # Authentication Settings
# AUTH_USER_MODEL = 'authtools.User'

LOGIN_URL = "login"

# LOGIN_URL = reverse("accounts:login")

THUMBNAIL_EXTENSION = 'png'  # Or any extn for your thumbnails

LOGIN_EXEMPT_URLS = (  # urls a user can access while they are logged out
    'account/signup/',
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Activate Django heroku
# django_heroku.settings(locals())
