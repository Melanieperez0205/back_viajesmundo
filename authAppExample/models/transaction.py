from django.db import models
from .account  import Account

class Transaction(models.Model):
    id              = models.AutoField(primary_key=True)
    inmueble_inicial  = models.ForeignKey(Account, related_name='Inmueble_inicial', on_delete=models.CASCADE)
    inmueble_final    = models.ForeignKey(Account, related_name='Inmuble_final', on_delete=models.CASCADE)
    register_date   = models.DateTimeField(auto_now_add=True, blank=True)
    note            = models.CharField(max_length=100)