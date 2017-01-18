from django.db import models
from enum import Enum


class Position(models.Model):
    """
    Информация о позиции в пространстве.
    Пока используем это, а не GeoDjango.
    Все числа - в метрах.
    """
    x = models.FloatField(default=0.0)
    y = models.FloatField(default=0.0)
    z = models.FloatField(default=0.0)

    def __str__(self):
        return 'Position(x={0}, y={1}, z={2})'.format(self.x, self.y, self.z)


class Sensor(models.Model):
    """
    Информация о сенсоре.

    position - позиция в пространстве
    radius - радиус действия (в метрах)
    heartbeat_interval - интервал в секундах между докладами о работоспособности
    state - текущее состояние
    """

    position = models.ForeignKey(Position)
    radius = models.FloatField(default=150)
    heartbeat_interval = models.PositiveSmallIntegerField(default=10)
    state = models.CharField(max_length=10, choices=(
        ('working', 'working'),
        ('waiting', 'waiting'),
        ('broken', 'broken')
    ), default='working')

    def __str__(self):
        return 'Sensor(position={0})'.format(self.position)
