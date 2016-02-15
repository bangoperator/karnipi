from django.contrib import admin
from terrarium.models import Terrarium, Heater, TerrariumLog


class HeaterInline(admin.StackedInline):
    model = Heater


class FoggerInline(admin.StackedInline):
    model = Heater


class TerrariumAdmin(admin.ModelAdmin):
    fields = ['title']
    inlines = [HeaterInline, FoggerInline]


class TerrariumLogAdmin(admin.ModelAdmin):
    fields = ['time', 'i2cDevice', 'temperature', 'humidity']

admin.site.register(Terrarium, TerrariumAdmin)
admin.site.register(TerrariumLog, TerrariumLogAdmin)
