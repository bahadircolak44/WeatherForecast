from django.db import models


class WorldCities(models.Model):
    city_name = models.CharField(max_length=64, null=False)

    class Meta:
        db_table = 'world_cities'

    @classmethod
    def generate(cls):
        import pandas as pd
        import json
        cities_csv = pd.read_csv("worldcities.csv")
        cities_json = json.loads(cities_csv.to_json())
        city_list = [cls(city_name=city) for city_id, city in cities_json.get('city_ascii').items()]
        cls.objects.bulk_create(city_list)
