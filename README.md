# nova-app_blog_migrations
Application for management works auxiliary worker.
Included folowing Applications:
  1 - personal_portfolio - "Main Application"
    1.1 - settings:
      INSTALLED_APPS = ['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes',
    'django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles',
    'blog.apps.BlogConfig','skills.apps.SkillsConfig','equipments.apps.EquipmentsConfig','works.apps.WorksConfig',]
    ROOT_URLCONF = 'personal_portfolio.urls
    # Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'ru-Ru'  TIME_ZONE = 'UTC'  USE_I18N = True  USE_TZ = True  
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'  STATIC_ROOT=BASE_DIR/'static'  MEDIA_URL = 'media/'  MEDIA_ROOT = BASE_DIR / 'media'
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
  2 - works - "Main Paige" = Task
  3 - equipments - "Page for Equipment"
  4 - skills - Worker's belonging to a special type of work.
  5 - blogs - Separate articles on the work of an Auxililary Workers.
