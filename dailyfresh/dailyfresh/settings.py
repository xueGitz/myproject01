"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_-k$^sx5n&0+i6^q@-mxj!24-3c)o+o(af%sa(8x$2gqp9c8=1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',

    "user",
    "goods",

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dailyfresh.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dailyfresh',
        'USER': 'root',
        'PASSWORD': '1234',
        'HOST': '192.168.12.155',
        'PORT': '3306',

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'
# LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# 存储静态文件
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# session 存入redis
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = ''
SESSION_REDIS_PREFIX = 'session'

AUTH_USER_MODEL= 'user.User'


# 配置发送邮件
# EMAIL_BACKEND = 'django.core.mail.stmp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '13523077502@163.com'
EMAIL_HOST_PASSWORD = '123456z'
EMAIL_FROM = '天天生鲜<13523077502@163.com>'

# 存储上传文件
MEDIA_ROOT=os.path.join(BASE_DIR,"static/media")

# 验证登录装饰器默认地址
LOGIN_URL = '/login'

# 使用富文本编辑器
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'width': 600,
    'height': 400,
}
