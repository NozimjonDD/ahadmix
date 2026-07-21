"""
Django settings for ahadmix project.
"""

from pathlib import Path

import environ
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

environ.Env.read_env(BASE_DIR / '.env')


SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')


INSTALLED_APPS = [
    # Unfold must come before django.contrib.admin — it overrides admin templates.
    'unfold',
    'unfold.contrib.filters',
    'unfold.contrib.forms',
    'unfold.contrib.inlines',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'common',
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

ROOT_URLCONF = 'ahadmix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'ahadmix.wsgi.application'


DATABASES = {
    'default': env.db('DATABASE_URL', default=f'sqlite:///{BASE_DIR / "db.sqlite3"}'),
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


LANGUAGE_CODE = env('LANGUAGE_CODE', default='en-us')

TIME_ZONE = env('TIME_ZONE', default='UTC')

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,
}



UNFOLD = {
    "SITE_TITLE": "Ahadmix Admin",
    "SITE_HEADER": "Ahadmix",
    "SITE_SUBHEADER": "Boshqaruv paneli",
    "SITE_URL": "/",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "SHOW_BACK_BUTTON": True,

    "COLORS": {
        # Tailwind-style palette; Unfold expects space-separated RGB channels.
        "primary": {
            "50": "240 249 255",
            "100": "224 242 254",
            "200": "186 230 253",
            "300": "125 211 252",
            "400": "56 189 248",
            "500": "14 165 233",
            "600": "2 132 199",
            "700": "3 105 161",
            "800": "7 89 133",
            "900": "12 74 110",
            "950": "8 47 73",
        },
    },

    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": "Sayt",
                "separator": False,
                "items": [
                    {
                        "title": "Sozlamalar",
                        "icon": "settings",
                        "link": lambda r: reverse_lazy("admin:common_sitesettings_changelist"),
                    },
                    {
                        "title": "Ekranlar",
                        "icon": "tv",
                        "link": lambda r: reverse_lazy("admin:common_monitor_changelist"),
                    },
                    {
                        "title": "Narx qatorlari",
                        "icon": "sell",
                        "link": lambda r: reverse_lazy("admin:common_monitorpricerow_changelist"),
                    },
                    {
                        "title": "Hamkorlar",
                        "icon": "handshake",
                        "link": lambda r: reverse_lazy("admin:common_partner_changelist"),
                    },
                ],
            },
            {
                "title": "Kontent",
                "separator": True,
                "items": [
                    {
                        "title": "Statistika",
                        "icon": "bar_chart",
                        "link": lambda r: reverse_lazy("admin:common_statisticcard_changelist"),
                    },
                    {
                        "title": "Nega biz",
                        "icon": "star",
                        "link": lambda r: reverse_lazy("admin:common_whyuscard_changelist"),
                    },
                    {
                        "title": "Jarayon",
                        "icon": "format_list_numbered",
                        "link": lambda r: reverse_lazy("admin:common_processcard_changelist"),
                    },
                    {
                        "title": "FAQ",
                        "icon": "help",
                        "link": lambda r: reverse_lazy("admin:common_faq_changelist"),
                    },
                ],
            },
            {
                "title": "Foydalanuvchilar",
                "separator": True,
                "items": [
                    {
                        "title": "Foydalanuvchilar",
                        "icon": "person",
                        "link": lambda r: reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Guruhlar",
                        "icon": "group",
                        "link": lambda r: reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}
