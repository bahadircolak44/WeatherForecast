import json

import requests
from django.conf import settings
from django.core.management import BaseCommand
from rest_framework import status

from api.models import WeatherForecast
from api.models import WorldCities


class Command(BaseCommand):
    """
    This command need to be run just once, python manage.py get_forecast.
    When you get all city forecasts, responses will be perform on db.
    If db is not up to date, service will be update itself.

    This command
    """
    def handle(self, *args, **options):
        city_list = WorldCities.objects.values('id', 'city_name')
        all_forecast_list = []
        for i, city in enumerate(city_list):
            print("Index:", i, "--  City:", city)
            response = requests.get(
                f"{settings.WORLD_WEATHER_ONLINE_BASE_URL}/?key={settings.WORLD_WEATHER_ONLINE_API_KEY}&"
                f"q={city.get('city_name')}&format={settings.WORLD_WEATHER_ONLINE_FORMAT}")
            if response.status_code == status.HTTP_200_OK:
                content = json.loads(response.content)
                all_forecast_list.append(
                    WeatherForecast(
                        city_id=city.get('id'),
                        forecast_data=content
                    )
                )
        WeatherForecast.objects.bulk_create(all_forecast_list)
