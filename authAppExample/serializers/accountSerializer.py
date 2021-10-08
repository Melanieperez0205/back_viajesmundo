from authAppExample.models.account import Account
from rest_framework                import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['habitaciones', 'banios', 'alimentacion','valoracion','precio','estado','descripcion','ubicacion','lastChangeDate']