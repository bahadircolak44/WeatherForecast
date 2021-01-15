import traceback

import requests
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serilaizers import WeatherConditionSerializer
from authentication.serializers import GenericModelSerializer


class WeatherConditionView(APIView):
    """

    """

    def get(self, *args, **kwargs):
        try:
            serializer = WeatherConditionSerializer(data=self.request.query_params)
            if serializer.is_valid():
                r = requests.get(
                    f"{settings.WORLD_WEATHER_ONLINE_BASE_URL}?key={settings.WORLD_WEATHER_ONLINE_API_KEY}&"
                    f"city={serializer.validated_data.get('city')}&format={settings.WORLD_WEATHER_ONLINE_FORMAT}")
                if not r.status_code == status.HTTP_200_OK:
                    return Response(status=status.HTTP_204_NO_CONTENT)

            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            print(traceback.format_exc())
            return Response(data=str(ex), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ListWorldCitiesView(APIView):
    """

    """

    def get(self, *args, **kwargs):
        try:
            serializer = GenericModelSerializer(data=self.request.query_params)
            if serializer.is_valid():
                pass
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
