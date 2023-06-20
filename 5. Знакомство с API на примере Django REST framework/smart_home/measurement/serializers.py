from rest_framework import serializers
from measurement.models import Sensor, Measurement


class SensorSer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ["id", "name", "description"]


class MeasurementSer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ["sensor", "temperature", "created_at", "image"]


class FullSensorSer(serializers.ModelSerializer):
    measurements = MeasurementSer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurements"]
