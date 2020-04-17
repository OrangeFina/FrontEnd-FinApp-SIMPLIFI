from rest_framework import serializers
from .models import Risk

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ['id', 'response']

class AlloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ['aType']
