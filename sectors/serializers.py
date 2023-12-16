from rest_framework import serializers
from .models import Sector


class CreateSectorSerializer(serializers.Serializer):
    agree = serializers.BooleanField()
    user_name = serializers.CharField()
    sectors = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )


class EditSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    sectors = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False
    )
