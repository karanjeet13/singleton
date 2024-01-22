from django.apps import AppConfig



class SingletonAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'singleton_app'

    def ready(self):
        try:
            import singleton_app.tests
        except ImportError as e:
            print(f"Error importing tests: {e}")
