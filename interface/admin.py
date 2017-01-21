from django.contrib import admin
from .models import Position, Sensor, SoundSource, World

# Register your models here.
admin.site.register(Position)
admin.site.register(Sensor)
admin.site.register(SoundSource)
admin.site.register(World)
