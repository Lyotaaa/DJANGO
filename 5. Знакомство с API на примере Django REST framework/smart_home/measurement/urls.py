from django.urls import path
from measurement.views import SensorView

urlpatterns = [
    path("sensors/", SensorView.as_view()),

]
