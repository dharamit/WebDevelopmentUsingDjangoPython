"""
Django settings for storytime project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fd@zm_0)hx(tede*(0&lwoa0@kijcvv%l6)-5x8!3xjh4+emx@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'story',
    'rest_framework',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
###############################
#Default
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (    
        '127.0.0.1',
    )
CORS_ALLOW_METHODS = (
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS'
    )

#CORS_ALLOW_ORIGIN       string            Access-Control-Allow-Origin
#CORS_ALLOW_METHODS      list              Access-Control-Allow-Methods
#CORS_ALLOW_HEADERS      list              Access-Control-Allow-Headers
#CORS_ALLOW_CREDENTIALS  "true" or "false" Access-Control-Allow-Credentials
#CORS_EXPOSE_HEADERS     list              Access-Control-Expose-Headers
#CORS_MAX_AGE            seconds           Access-Control-Max-Age
#CORS_ALLOW_ALL_ORIGIN   <any-value>       <see explanation below>
#CORS_ALLOW_ALL_HEADERS  <any-value>       <see explanation below>

ROOT_URLCONF = 'storytime.urls'

WSGI_APPLICATION = 'storytime.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#'django.db.backends.sqlite3',
        'NAME': 'POCKETCHEF',#os.path.join(BASE_DIR, 'mysql'),#os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'root',
        'PASSWORD': 'natalie',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = '/home/amit/storytime/storytime/static/static_root'
STATIC_ROOT=os.path.join(BASE_DIR,'storytime','static','static_root')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'storytime','static','static_dir'),
    #'/home/amit/storytime/storytime/static/static_dir'
    )