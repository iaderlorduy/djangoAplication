from django.contrib import admin
from Registro.models import Proyecto, Categoria, Perfil
# Register your models here.

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('usuario','nombre','id_categoria')
    list_filter = ('id_categoria','nombre')
    search_fields = ['nombre', 'usuario']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('get_nombre', 'get_email')
    search_fields = ['usuario__username']

    def get_nombre(self, obj):
      return obj.usuario.username

    def get_email(self, obj):
      return obj.usuario.email

    get_nombre.short_description = 'usuario'
    get_email.short_description = 'email'

class PerfilAdmin(admin.ModelAdmin):
  list_display = ('user','nombre', 'direccion', 'edad', 'fechaingreso','imagen')
  list_filter = ('nombre','edad')
  search_fields = ['nombre', 'fechaingreso']


admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Perfil, PerfilAdmin)