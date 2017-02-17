from django.contrib import admin
from .models import (Position, Sensor, SoundSource, World, Computer, NetworkAdapter, SoftwareState, IntBound,
                     IntInterval, NetworkConnection)

# Register your models here.
admin.site.register(Position)
admin.site.register(Sensor)
admin.site.register(SoundSource)
admin.site.register(World)

admin.site.register(Computer)
admin.site.register(NetworkAdapter)
admin.site.register(SoftwareState)
admin.site.register(IntBound)

admin.site.register(IntInterval)
admin.site.register(NetworkConnection)
