import os
from pathlib import Path

# ✅ Rutas base
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Seguridad
SECRET_KEY = 'django-insecure-5z1hu!5@*pvr88enaz!$19s1vyd7x)7l75=x7fe^5t^bycyzv^'
DEBUG = True
ALLOWED_HOSTS = []

# ✅ Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gastos',   # ✅ App de gastos
    'ingresos',  # ✅ App de ingresos
]

# ✅ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ✅ Configuración de URLs
ROOT_URLCONF = 'gestor_de_gastos.urls'

# ✅ Configuración de Plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'gestor_de_gastos', 'templates'),  # 📂 Plantillas globales
            os.path.join(BASE_DIR, 'gastos', 'templates'),  # 📂 Plantillas de gastos
            os.path.join(BASE_DIR, 'ingresos', 'templates'),  # 📂 Plantillas de ingresos
        ],
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

# ✅ Configuración de WSGI
WSGI_APPLICATION = 'gestor_de_gastos.wsgi.application'

# ✅ Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ✅ Validaciones de Seguridad
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ✅ Configuración de Idioma y Zona Horaria
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

# ✅ Archivos Estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'gestor_de_gastos', 'static'),  # 📂 Carpeta de archivos estáticos globales
]

# ✅ Archivos Multimedia (para imágenes u otros archivos subidos)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ✅ Configuración de Claves Primarias
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
