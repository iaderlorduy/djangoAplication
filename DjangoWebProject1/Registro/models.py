from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(User)
    nombre = models.CharField(max_length=50, blank = True , unique=True)
    apellido = models.CharField(max_length=50, blank = True , unique=True)
    descripcion = models.TextField(max_length=50, blank = True)
    fecha_creacion = models.DateTimeField(auto_now=True)
    pais = models.CharField(max_length=50, blank = True)
    ciudad = models.CharField(max_length=50, blank = True)
    email = models.CharField(max_length=50, blank = True)
    imagen = models.ImageField(upload_to = 'persona', blank = True)
    def __unicode__(self): return self.nombre


class Categoria(models.Model):
	id_categoria = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=50, blank = True , unique=True)
	activo = models.BooleanField(default = False)
	fecha_creacion = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.nombre

class Patrocinio(models.Model):
	id_patrocinado = models.ForeignKey(Persona, related_name='id_patrocinado')
	id_patrocinador = models.ForeignKey(Persona, related_name='id_patrocinador')
	id_categoria = models.ForeignKey(Categoria)
	fecha_patrocinio = models.DateField(auto_now = True)
	razon_patrocinio = models.TextField(max_length=50, blank = True)
        def __unicode__(self): return self.razon_patrocinio
        