from rest_framework import serializers
from django.db.models import Model, IntegerField, TextField, FileField
from django_mysql.models import JSONField
from .models import Data, DataCheck


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"


class DataCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataCheck
        fields = "__all__"
