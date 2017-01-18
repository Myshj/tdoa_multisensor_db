from .models import Position, Sensor
from rest_framework import serializers
from enumfields import EnumField


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('x', 'y', 'z')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('position', 'radius', 'heartbeat_interval', 'state')
