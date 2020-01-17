from rest_framework import serializers

from .models import Enum


class EnumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enum
        fields = '__all__'
