# Import necessary modules
import dj_database_url
from pathlib import Path
import os
from .base import *

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Set DEBUG to False
DEBUG = False

# Replace the SQLite DATABASES configuration with PostgreSQL:
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        # default='postgresql://postgres:postgres@localhost:5432/mysite',
        default='postgresql://fintech_app_user:EY6zLm8B1QhfqIDFrQtfnDFWOR8FMrlV@dpg-cst66brtq21c73a7rptg-a/fintech_app',
        conn_max_age=600,
        conn_health_checks=True,
        )
}

# Add the necessary middleware
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


# Set the static URL
STATIC_URL = '/static/'

# Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
# and renames the files with unique names for each version to support long-term caching
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

WHITENOISE_MANIFEST_STRICT = False

ALLOWED_HOSTS = ['online-banking-p6mb.onrender.com']