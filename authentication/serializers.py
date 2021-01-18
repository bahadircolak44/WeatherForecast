from django.contrib.auth.models import User
from rest_framework import serializers


class GenericModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # for re-usability
        self.Meta.fields = None
        self.Meta.exclude = None
        extra_fields = kwargs.pop('extra_fields', None)  # If you need more fields other than model
        model = kwargs.pop('model', None)
        fields = kwargs.pop('fields', None)
        exclude = kwargs.pop('exclude', None)
        if fields:
            self.Meta.fields = fields
        elif exclude:
            self.Meta.exclude = exclude
        if model:
            self.Meta.model = model
        if extra_fields:
            for _field, _value in extra_fields.items():
                self.fields[_field] = _value
        super().__init__(*args, **kwargs)

    class Meta:
        pass


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password', 'username')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)