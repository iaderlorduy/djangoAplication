from django.db import models
from django.contrib.auth.models import User
import uuid

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


TIPO_FACTURA = (
    ('ACUEDUCTO'     , 'ACUEDUCTO'     ),
    ('ALCANTARILLADO', 'ALCANTARILLADO'),
    ('ASEO'          , 'ASEO'          ),
    ('ELECTRICA'     , 'ELECTRICA'     ),
    ('GAS'           , 'GAS'           ),
)

TIPO_PETICION = (
    ('DENUCIAS'     , 'DENUCIAS'     ),
    ('PETICIONES', 'PETICIONES'),
    ('QUEJAS'          , 'QUEJAS'          ),
    ('RECLAMO'     , 'RECLAMO'     ),
    ('SUGERENCIA'           , 'SUGERENCIA'           ),
)

ESTADO_FACTURA = (
    ('CREADA'     , 'CREADA'     ),
    ('PAGADA', 'PAGADA'),
    ('ANULADA'          , 'ANULADA'          ),
)

def my_random_key():
    return uuid.uuid4()

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    tipo_factura = models.CharField(max_length=50, choices=TIPO_FACTURA, default='CREADA')
    codigo = models.CharField(max_length=48, default=my_random_key)
    usuario = models.ForeignKey(User)
    fecha_emision = models.DateTimeField(auto_now=True)
    fecha_vencimiento = models.DateTimeField(auto_now=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(max_length=50, blank = True)
    estado_factura = models.CharField(max_length=50, choices=ESTADO_FACTURA, default=1)
    def __unicode__(self): return self.usuario.username

class Peticion(models.Model):
    id_peticion = models.AutoField(primary_key=True)
    tipo_peticion = models.CharField(max_length=50, choices=TIPO_PETICION, default=1)
    descripcion = models.TextField(max_length=50, blank = True)
