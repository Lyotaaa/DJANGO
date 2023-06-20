from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=113, verbose_name="Название датчика")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Датчик"
        verbose_name_plural = "Датчики"

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="measurements",
        verbose_name="Датчик",
    )
    temperature = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name="Температура"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата измерения")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")


# Sensor(name="Кухня", description="Датчик на кухне").save()
# Measurement(temperature = 22.2, image = "", sensor_id = ..)
