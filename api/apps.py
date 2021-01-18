from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self, *args, **kwargs):
        from django.contrib.auth.models import User
        from .models import WorldCities
        world_cities = WorldCities.objects.all().exists()
        if not world_cities:
            WorldCities.generate()
        users = User.objects.all().exists()
        if not users:
            User.objects.create_superuser('test', 'bahdrcolak@gmail.com', 'test')
