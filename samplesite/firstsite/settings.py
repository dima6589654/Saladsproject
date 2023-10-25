"""
Django settings for firstsite project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'template_profiler_panel',
    'bootstrap4',
    'captcha',
    'precise_bbcode',
    'django_cleanup',
    'easy_thumbnails',
    'django_redis',
    'rest_framework',
    'corsheaders',

    'bboard.apps.BboardConfig',
    'testapp.apps.TestappConfig',
    'authapp',
    'userapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'bboard.middlewares.my_middleware',
    # 'bboard.middlewares.MyMiddleware',
    # 'bboard.middlewares.RubricsMiddleware',
]

ROOT_URLCONF = 'firstsite.urls'

AUTH_USER_MODEL = 'userapp.BbUser'

# ABSOLUTE_URL_OVERRIDES = {
#     # 'bboard.rubric': lambda rec: "/bboard/%s/" % rec.pk,
#     # 'bboard.rubric': lambda rec: f"/bboard/{rec.pk}/",
#     'bboard.rubric': lambda rec: f"/{rec.pk}/",
# }

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [BASE_DIR / 'templates'],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'bboard.context_processors.rubrics',
            ],
            # 'libraies': {
            #     'filtersandtags': 'bboard.filtersandtags',
            #     'ft': 'bboard.filtersandtags',
            # },
            # 'builtins': [
            #     'bboard.filtersandtags',
            # ]
        },
    },
]

WSGI_APPLICATION = 'firstsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #     # 'ATOMIC_REQUESTS': True,
    #     # 'AUTOCOMMIT': True,
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "firstsite",
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASS"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # 'OPTIONS': {'max_similarity': 0.7},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # 'OPTIONS': {'min_length': 8},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # 'OPTIONS': {'password_list_path': 'какой-то путь'},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'firstsite.validators.NoForbiddenCharsValidator',
        'OPTIONS': {'forbidden_chars': (' ', ',', '.', ':', ';')},
    },
]

DEFAULT_CHARSET = 'utf-8'


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static_prod')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

LOGOUT_REDIRECT_URL = 'index'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Настройки Капчи
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 6
CAPTCHA_TIMEOUT = 10
CAPTCHA_LETTER_ROTATION = (-15, 15)
CAPTCHA_BACKGROUND_COLOR = '#001100'
CAPTCHA_FOREGROUND_COLOR = '#FFFFFF'

BBCODE_SMILIES_UPLOAD_TO = "static/precise_bbcode/smilies"
# BBCODE_ALLOW_SMILIES = False


THUMBNAIL_ALIASES = {
    'bboard.Bb.picture': {
        'default': {
            'size': (500, 300),
            'crop': 'scale',
        },
    },
    'testapp': {
        'default': {
            'size': (400, 300),
            'crop': 'smart',
            'bw': True,
        },
    },
    '': {
        'default': {
            'size': (180, 240),
            'crop': 'scale',
        },
        'big': {
            'size': (480, 640),
            'crop': '10,10',
        }
    },
}

THUMBNAIL_DEFAULT_OPTIONS = {
    'quality': 90,
    'subsampling': 1,
}

THUMBNAIL_BASEDIR = 'thumbs'

# DOMAIN_NAME = 'HTTP://127.0.0.1:8000'
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# DEFAULT_FROM_EMAIL = "webmaster@localhost"
# EMAIL_HOST = "localhost"
# EMAIL_PORT = 25
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# EMAIL_USE_SSL = False
# EMAIL_USE_TLS = False
# EMAIL_SSL_CERTFILE = None
# EMAIL_SSL_KEYFILE = None
# EMAIL_TIMEOUT = None
EMAIL_USE_LOCALE = True
EMAIL_FILE_PATH = "tmp/messages/"

ADMINS = [
    ('Admin1', 'admin1@supersite.ru'),
    ('Admin2', 'admin2@supersite.ru'),
    ('MegaAdmin', 'megaadmin@supersite.ru'),
]

INTERNAL_IPS = [
    "127.0.0.1",
]

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'cache_table',
#         'TIMEOUT': 120,
#         'OPTIONS': {
#             'MAX_ENTRIES': 200,
#         }
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
#         'LOCATION': '127.0.0.1:11211',  # 'LOCATION': 'localhost:11211',
#     }
# }

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': os.path.join(BASE_DIR, 'file_cache'),
#     }
# }

# Настройки для кэширования
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Адрес и порт вашего Redis-сервера
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
#
# # Настройки для хранения сессий в Redis
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
#
# # Настройки для работы с очередями задач (не обязательно)
# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/2'  # Адрес и порт вашего Redis-сервера

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:5500',
    'http://localhost:5500',
]

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }


# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
# def info_filter(message):
#     return message.levelname == 'INFO'


LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "simple": {
            'format': '[%(asctime)s] %(levelname)s %(message)s',
            'datefmt': '%Y.%m.%d %H:%M:%S',
        },
    },
    "filters": {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        # 'info_filter': {
        #     '()': 'django.utils.log.CallbackFilter',
        #     'callback': info_filter,
        # }
    },
    "handlers": {
        'console_dev': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'filters': ['require_debug_true'],
        },
        'console_prod': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'ERROR',
            'filters': ['require_debug_false'],
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/django-site.log',
            'maxBytes': 1048576,
            'backupCount': 10,
            'formatter': 'simple',
        }
    },
    "loggers": {
        'django': {
            'handlers': ['console_dev', 'console_prod'],
        },
        'django.server': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
