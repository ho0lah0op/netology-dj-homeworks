# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class TemperatureMeasurementCreateView(generics.CreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorMeasurementsView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


