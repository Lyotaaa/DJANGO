# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import (
    SensorDetailSerializer,
    SensorSerializer,
    MeasurementSerializer,
)


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class CreateSensorVeiw(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
