from .models import (Position, Sensor, SoundSource, World, Computer, NetworkAdapter, IntBound,
                     IntInterval, NetworkConnection)
from rest_framework import viewsets
from .serializers import (PositionSerializer, SensorSerializer, SoundSourceSerializer, WorldSerializer, ComputerSerializer,
                          IntBoundSerializer, IntIntervalSerializer, NetworkAdapterSerializer,
                          NetworkConnectionSerializer)
from django.shortcuts import redirect
from django.db import transaction


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SoundSourceViewSet(viewsets.ModelViewSet):
    queryset = SoundSource.objects.all()
    serializer_class = SoundSourceSerializer


class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class IntBoundViewSet(viewsets.ModelViewSet):
    queryset = IntBound.objects.all()
    serializer_class = IntBoundSerializer


class IntIntervalViewSet(viewsets.ModelViewSet):
    queryset = IntInterval.objects.all()
    serializer_class = IntIntervalSerializer


class NetworkAdapterViewSet(viewsets.ModelViewSet):
    queryset = NetworkAdapter.objects.all()
    serializer_class = NetworkAdapterSerializer


class NetworkConnectionViewSet(viewsets.ModelViewSet):
    queryset = NetworkConnection.objects.all()
    serializer_class = NetworkConnectionSerializer


def reset(request):
    count_of_sensors_in_row = 5

    Sensor.objects.all().delete()
    Position.objects.all().delete()
    Computer.objects.all().delete()
    NetworkAdapter.objects.all().delete()
    IntBound.objects.all().delete()
    IntInterval.objects.all().delete()
    NetworkConnection.objects.all().delete()
    world = World.objects.all()[0]

    # СОЗДАЛИ ПОЗИЦИИ ДЛЯ ДАТЧИКОВ
    Position.objects.bulk_create([
                                     Position(
                                         x=i * 50,
                                         y=j * 100 if j % 2 == 0 else j * 100 + 50,
                                         z=0.0
                                     )
                                     for i in range(0, count_of_sensors_in_row)
                                     for j in range(0, count_of_sensors_in_row)
                                     ])
    sensor_positions = Position.objects.all()

    # СОЗДАЛИ ДАТЧИКИ
    Sensor.objects.bulk_create([
                                   Sensor(
                                       world=world,
                                       position=sensor_positions[i]
                                   ) for i in range(0, count_of_sensors_in_row * count_of_sensors_in_row)
                                   ])
    sensors = Sensor.objects.all()

    # СОЗДАЛИ СЕТЕВЫЕ АДАПТЕРЫ
    NetworkAdapter.objects.bulk_create([
                                           NetworkAdapter(
                                               world=world,
                                               position=sensor_positions[i]
                                           ) for i in range(0, count_of_sensors_in_row * count_of_sensors_in_row)
                                           ])
    sensor_controllers_network_adapters = NetworkAdapter.objects.all()

    # СОЗДАЛИ КОНТРОЛЛЕРЫ ДАТЧИКОВ
    Computer.objects.bulk_create([
                                     Computer(
                                         world=world,
                                         position=sensor_positions[i],
                                         is_active_sensor_controller=True,
                                         is_active_tdoa_controller=False
                                     ) for i in range(0, count_of_sensors_in_row * count_of_sensors_in_row)
                                     ])
    sensor_controllers = Computer.objects.all()

    # ПОДКЛЮЧИЛИ ДАТЧИКИ И СЕТЕВЫЕ АДАПТЕРЫ К КОНТРОЛЛЕРАМ
    with transaction.atomic():
        for i, sensor_controller in enumerate(sensor_controllers):
            sensor_controller.network_adapters.add(sensor_controllers_network_adapters[i])
            sensor_controller.sensors.add(sensors[i])

    # СОЗДАЛИ СЕРВЕР-КОНТРОЛЛЕР 5-к
    tdoa_controller_position = Position(x=999999, y=999999, z=0)
    tdoa_controller_position.save()
    tdoa_controller_adapter = NetworkAdapter(world=world, position=tdoa_controller_position)
    tdoa_controller_adapter.save()
    tdoa_controller_server = Computer(
        world=world,
        position=tdoa_controller_position,
        is_active_tdoa_controller=True,
        is_active_sensor_controller=False
    )
    tdoa_controller_server.save()
    tdoa_controller_server.network_adapters.add(tdoa_controller_adapter)
    tdoa_controller_server.save()

    # СОЗДАЛИ СЕРВЕР-ФИЛЬТР ПОТОКА СООБЩЕНИЙ О ПОЗИЦИЯХ
    position_determinator_positiion = Position(x=888888, y=888888, z=0)
    position_determinator_positiion.save()
    position_determinator_adapter = NetworkAdapter(world=world, position=position_determinator_positiion)
    position_determinator_adapter.save()
    position_determinator_server = Computer(
        world=world,
        position=position_determinator_positiion,
        is_active_position_determinator=True
    )
    position_determinator_server.save()
    position_determinator_server.network_adapters.add(position_determinator_adapter)
    position_determinator_server.save()

    # СОЗДАЛИ СОЕДИНЕНИЯ ОТ ДАТЧИКОВ К КОНТРОЛЛЕРУ 5-К
    left_latency_bound = IntBound(value=30, bound_type='inclusive')
    right_latency_bound = IntBound(value=150, bound_type='inclusive')
    left_latency_bound.save()
    right_latency_bound.save()

    latency_interval = IntInterval(lower_bound=left_latency_bound, upper_bound=right_latency_bound)
    latency_interval.save()

    NetworkConnection.objects.bulk_create([
                                              NetworkConnection(
                                                  adapter_from=sensor_controller.network_adapters.all()[0],
                                                  adapter_to=tdoa_controller_server.network_adapters.all()[0],
                                                  possible_latency=latency_interval
                                              ) for sensor_controller in sensor_controllers
                                              ])

    # СОЗДАЛИ СОЕДИНЕНИЕ ОТ КОНТРОЛЛЕРА 5-К К ФИЛЬТРУ ПОТОКА СООБЩЕНИЙ О ПОЗИЦИЯХ
    left_latency_bound = IntBound(value=30, bound_type='inclusive')
    right_latency_bound = IntBound(value=150, bound_type='inclusive')
    left_latency_bound.save()
    right_latency_bound.save()

    latency_interval = IntInterval(lower_bound=left_latency_bound, upper_bound=right_latency_bound)
    latency_interval.save()
    conn = NetworkConnection(
        adapter_from=tdoa_controller_adapter,
        adapter_to=position_determinator_adapter,
        possible_latency=latency_interval
    )

    # СОЗДАЛИ ИСТОЧНИК ЗВУКА
    sound_source_position = Position(x=129, y=130)
    sound_source_position.save()
    sound_source = SoundSource(
        position=sound_source_position,
        world=world,
        interval=10
    )
    sound_source.save()

    return redirect('/')
