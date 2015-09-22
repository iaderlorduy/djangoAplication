from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
	usuario = models.OneToOneField(User)
	id_proyecto = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50, blank = True , unique=True)
	fecha_creacion = models.DateTimeField(auto_now=True)
	pais = models.CharField(max_length=50, blank = True)
	ciudad = models.CharField(max_length=50, blank = True)
	email = models.CharField(max_length=50, blank = True)
	descripcion = models.TextField(max_length=50, blank = True)
	id_categoria = models.ForeignKey('Categoria', null = True,  blank = True)
	def __unicode__(self):
		return self.nombre


class Categoria(models.Model):
	id_categoria = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50, blank = True , unique=True)
	activo = models.BooleanField(default = False)
	fecha_creacion = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.nombre

class Perfil(models.Model):
	user = models.ForeignKey(User)
	nombre = models.CharField(max_length = 20)
	direccion = models.CharField(max_length = 50, blank = True)
	edad = models.IntegerField(blank = True)
	fechaingreso = models.DateField(auto_now = True)
	imagen = models.ImageField(upload_to = 'perfil', blank = True)

	def __unicode__(self):
		return self.user.username