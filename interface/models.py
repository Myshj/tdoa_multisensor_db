from django.db import models


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


class World(models.Model):
    """
    Информация о среде, к которой прикреплены сенсоры и источники звука.

    name - название мира.
    speed_of_sound - скорость звука в метрах в секунду
    """
    name = models.CharField(max_length=100)
    speed_of_sound = models.FloatField(default=340.29)

    def __str__(self):
        return 'World(name={0}, speed_of_sound={1})'.format(self.name, self.speed_of_sound)


class WorldRelated(models.Model):
    """
    Информация о принадлежности к миру.

    position - позиция в пространстве
    world - к какому миру относимся
    """

    position = models.ForeignKey(Position)
    world = models.ForeignKey(World)

    class Meta:
        abstract = True


class NetworkAdapter(WorldRelated):
    """
    Информация о сетевом адаптере.
    """

    def __str__(self):
        return 'NetworkAdapter(position={0})'.format(self.position)


class Sensor(WorldRelated):
    """
    Информация о сенсоре.

    radius - радиус действия (в метрах)
    heartbeat_interval - интервал в секундах между докладами о работоспособности
    failure_probability - вероятность поломки в каждую секунду
    state - текущее состояние
    """

    radius = models.FloatField(default=150)
    heartbeat_interval = models.PositiveSmallIntegerField(default=10)
    state = models.CharField(max_length=10, choices=(
        ('working', 'working'),
        ('waiting', 'waiting'),
        ('broken', 'broken')
    ), default='working')
    failure_probability = models.FloatField(default=0.0001)

    def __str__(self):
        return 'Sensor(position={0})'.format(self.position)


class Computer(WorldRelated):
    """
    Информация о компьютере.

    sensors - с каких датчиков напрямую поступают данные
    network_adapters - какие подключены сетевые адаптеры
    """
    sensors = models.ManyToManyField(Sensor)
    network_adapters = models.ManyToManyField(NetworkAdapter)

    is_active_sensor_controller = models.BooleanField(default=False)
    is_active_tdoa_controller = models.BooleanField(default=False)
    is_active_position_determinator = models.BooleanField(default=False)

    def __str__(self):
        return 'Computer(position={0})'.format(self.position)


class SoundSource(WorldRelated):
    """
    Информация об источнике звука.

    interval - интервал в секундах между генерациями сигнала
    state - текущее состояние
    """

    interval = models.FloatField(default=10)
    state = models.CharField(max_length=10, choices=(
        ('working', 'working'),
        ('waiting', 'waiting'),
        ('broken', 'broken')
    ), default='working')

    def __str__(self):
        return 'SoundSource(position={0})'.format(self.position)


class IntBound(models.Model):
    """
    Информация о целочисленной границе.

    value - значение
    bound_type - открытая млм закрытая граница
    """
    value = models.IntegerField()
    bound_type = models.CharField(max_length=10, choices=(
        ('inclusive', 'inclusive'),
        ('exclusive', 'exclusive'),
    ), default='inclusive')

    def __str__(self):
        return 'IntBound(value={0}, bound_type={1})'.format(self.value, self.bound_type)


class IntInterval(models.Model):
    """
    Информация о целочисленном интервале.

    lower_bound - нижняя граница интервала
    upper_bound - верхняя граница интервала
    """
    lower_bound = models.ForeignKey(IntBound, related_name='lower_bound')
    upper_bound = models.ForeignKey(IntBound, related_name='upper_bound')

    def __str__(self):
        return 'IntInterval(lower_bound={0}, upper_bound={1})'.format(self.lower_bound.value, self.upper_bound.value)


class NetworkConnection(models.Model):
    """
    Информация о сетевом соединении между адаптерами.

    adapter_from - начальные адаптер
    adapter_to - конечный адаптер
    possible_latency - границы возможной задержки передачи данных в милисекундах
    """
    adapter_from = models.ForeignKey(NetworkAdapter, related_name='adapter_from')
    adapter_to = models.ForeignKey(NetworkAdapter, related_name='adapter_to')
    possible_latency = models.ForeignKey(IntInterval)

    def __str__(self):
        return """
        NetworkConnection(
        adapter_from={0},
        adapter_to={1},
        possible_latency={2}
        )
        """.format(self.adapter_from_id, self.adapter_to_id, self.possible_latency)
