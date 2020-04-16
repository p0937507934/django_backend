from rest_framework import serializers
from .models import Config


class ConfigSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = "__all__"