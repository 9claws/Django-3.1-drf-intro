from django.urls import path
from measurement.views import SensorView, SensorUpdateView, MeasurementView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]