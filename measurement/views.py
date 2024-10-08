from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        measure = MeasurementSerializer(data=request.data)
        if measure.is_valid():
            measure.save()
        return Response(data=measure.data)