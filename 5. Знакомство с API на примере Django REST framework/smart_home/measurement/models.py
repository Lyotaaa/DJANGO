from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    title = models.CharField(max_length=113, verbose_name="Название датчика")
    text = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.title

class Measuring(models.Model):
    sensor = models.ForeignKey(on_delete=models.CASCADE, related_name="sensor", verbose_name="Датчик")э
    temperature = models.TextField(verbose_name="Температура")
    measurement_date = models.DateTimeField(verbose_name="Дата измерения")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")