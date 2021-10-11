from django.db import models
from .user     import User

class Account(models.Model):
    id             = models.AutoField(primary_key=True)
    user           = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    habitaciones   = models.IntegerField(default=0)
    banios         = models.IntegerField(default=0)
    alimentacion   = models.BooleanField(default=True)      
    valoracion     = models.IntegerField(default=0.0)
    precio         = models.IntegerField(default=0)
    estado         = models.BooleanField(default=True)
    descripcion    = models.CharField('Descripcion inmueble', max_length=50,default='')
    ubicacion      = models.CharField('Ubicacion inmueble', max_length=50,default='')
    lastChangeDate = models.DateTimeField()
    isAvalaible = models.BooleanField(default=True)