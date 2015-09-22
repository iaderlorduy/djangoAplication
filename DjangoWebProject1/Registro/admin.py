from django.contrib import admin
from Registro.models import Persona, Categoria, Patrocinio
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','descripcion')
    list_filter = ('nombre','apellido')
    search_fields = ['nombre', 'usuario']

#class CategoriaAdmin(admin.ModelAdmin):
#    list_display = ('get_nombre', 'get_email')
#    search_fields = ['usuario__username']

#    def get_nombre(self, obj):
#      return obj.usuario.username

#    def get_email(self, obj):
#      return obj.usuario.email

#    get_nombre.short_description = 'usuario'
#    get_email.short_description = 'email'

class PatrocinioAdmin(admin.ModelAdmin):
    list_display = ('razon_patrocinio','fecha_patrocinio')


admin.site.register(Persona, PersonaAdmin)
admin.site.register(Patrocinio,PatrocinioAdmin)
admin.site.register(Categoria)