from django.apps import AppConfig


class TablesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tables'
    
    def ready(self):
        # Import models to ensure they're registered
        import tables.users  # noqa: F401
        import tables.recipes  # noqa: F401
        import tables.ingredients  # noqa: F401

