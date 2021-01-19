from django.urls import path

from api.views import ListWorldCitiesView, WeatherConditionView

urlpatterns = [
    path('cities/', ListWorldCitiesView.as_view()),
    path('weather-forecast/', WeatherConditionView.as_view()),
]
