# Localization

Django çoklu dil bir demo uygulamasıdır.

# Adım 1: Settings Dosyasını ayarlama
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', _('English')),
    ('tr', _('Turkish')),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Adım 2: Locale klasoründe dil dosyalarını oluşturma

python .\manage.py makemessages -l en --ignore=venv/*
python .\manage.py makemessages -l tr --ignore=venv/*

python .\manage.py compilemessages  --ignore=venv/*

# Adım 3: URL ayarlama

urlpatterns += i18n_patterns (
   path('', include("lang.urls"))
)

