# # TODO: опишите необходимые сериализаторы
from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement


class MeasurementSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(queryset=Sensor.objects.all())

    class Meta:
        model = TemperatureMeasurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


