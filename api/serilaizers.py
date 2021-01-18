from rest_framework import serializers


class NoModelSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class WeatherConditionSerializer(NoModelSerializer):
    city_name = serializers.CharField(required=True, allow_blank=False)
