from django.contrib import admin
from Registro.models import Persona, Factura
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','descripcion','email')
    list_filter = ('nombre','apellido')
    search_fields = ['nombre', 'usuario']


class FacturaAdmin(admin.ModelAdmin):
    list_display = ('tipo_factura','usuario','fecha_emision','fecha_vencimiento','descripcion')
    list_filter = ('tipo_factura','usuario','fecha_emision','fecha_vencimiento','descripcion')
    search_fields = ('fecha_emision','fecha_vencimiento')



admin.site.register(Persona, PersonaAdmin)
admin.site.register(Factura, FacturaAdmin)
