from django.contrib import admin
from .models import (Position, Sensor, SoundSource, World, WorldRelated, NetworkAdapter, HasNetworkAdapter, IntBound,
                     IntInterval, NetworkConnection)

# Register your models here.
admin.site.register(Position)
admin.site.register(Sensor)
admin.site.register(SoundSource)
admin.site.register(World)

#admin.site.register(WorldRelated)  abstract
admin.site.register(NetworkAdapter)
#admin.site.register(HasNetworkAdapter) abstract
admin.site.register(IntBound)

admin.site.register(IntInterval)
admin.site.register(NetworkConnection)
