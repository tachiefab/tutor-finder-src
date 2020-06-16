"""
Django settings for freelancer project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0.4/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0.4/ref/settings/
"""

import os
# from freelancer.aws.conf import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0.4/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'di9bzu*c&h19_i1dgg4ck0-nnsjtmb&t@h9q18c_$@98_!4lj2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'TutorfinderGh@gmail.com'
EMAIL_HOST_PASSWORD = 'TutorfinderGh@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    'phonenumber_field',
    'django_filters',
    'rest_framework',
    # 'sorl.thumbnail',
     #my apps
    'accounts',
    'analytics',
    # 'tutor',
    'locations',
    'subjects',

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

ROOT_URLCONF = 'freelancer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'freelancer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0.4/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0.4/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0.4/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0.4/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")
PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "protected")


# Custom Django auth settings

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'profile'

LOGOUT_REDIRECT_URL = 'index'


#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap4'



