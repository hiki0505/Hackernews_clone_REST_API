from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"

    def ready(self):
        print('Starting Scheduler...')
        from .upvotes_reset import upvotes_resetter
        upvotes_resetter.start()

