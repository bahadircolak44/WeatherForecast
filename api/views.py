import json
import traceback

import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import WorldCities
from api.serilaizers import WeatherConditionSerializer
from authentication.serializers import GenericModelSerializer


class WeatherConditionView(APIView):
    """
    @request http://127.0.0.1:8000/api/weather-forecast/?city=Ankara

    To get weather-forecast of given city
    """

    def post(self, *args, **kwargs):
        try:
            serializer = WeatherConditionSerializer(data=self.request.data)
            if serializer.is_valid():
                # Check if city exists
                world_city = WorldCities.objects.filter(**serializer.validated_data).exists()
                if world_city:
                    # send get request
                    response = requests.get(
                        f"{settings.WORLD_WEATHER_ONLINE_BASE_URL}/?key={settings.WORLD_WEATHER_ONLINE_API_KEY}&"
                        f"q={ serializer.validated_data.get('city_name')}&format={settings.WORLD_WEATHER_ONLINE_FORMAT}")
                    # Check if valid
                    if not response.status_code == status.HTTP_200_OK:
                        return Response(status=status.HTTP_204_NO_CONTENT)

                    content = json.loads(response.content)
                    return Response(content, status=status.HTTP_200_OK)
                return Response(data={}, status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(traceback.format_exc())
            return Response(data=str(ex), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListWorldCitiesView(APIView):
    """

    """

    def post(self, *args, **kwargs):
        try:
            serializer = GenericModelSerializer(data=self.request.data, model=WorldCities,
                                                fields=('id', 'city_name'))
            if serializer.is_valid():
                city_list = WorldCities.objects.filter(
                    city_name__contains=serializer.validated_data.get('city_name').capitalize()).values_list(
                    'city_name', flat=True)
                return Response(city_list)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            # For error.log
            print(traceback.format_exc())
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
