from django.urls import path
from measurement.views import SensorsView, SensorDetailView, CreateSensorVeiw

urlpatterns = [
    path("sensors/", SensorsView.as_view()),
    path("sensors/<int:pk>", SensorDetailView.as_view()),
    path("meas/", CreateSensorVeiw.as_view()),
]
