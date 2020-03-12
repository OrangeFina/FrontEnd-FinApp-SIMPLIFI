from rest_framework import serializers
from .models import Stock


class StockSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    ticker = serializers.CharField(max_length=10)
    desc = serializers.CharField(max_length=100)
    remarks = serializers.CharField(max_length=200)
    date = serializers.DateTimeField(auto_now_add=True)

    def create(self, validated_data):
        return Stock.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.ticker = validated_data.get('ticker', instance.name)
        instance.desc = validated_data.get('desc', instance.name)
        instance.remarks = validated_data.get('remarks', instance.name)
        instance.save()
        return instance