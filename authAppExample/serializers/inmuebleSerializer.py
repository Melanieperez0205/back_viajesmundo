from authAppExample.models.inmueble import Account
from rest_framework                import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Account
        fields = ['habitaciones', 'banios', 'alimentacion','valoracion','precio','descripcion','ubicacion','lastChangeDate','isAvailable']

    def to_representation(self, obj):
        inmueble = Account.objects.get(id=obj.id)
        return{
            "id"             : inmueble.id,
            "id_inmuebles"   : inmueble.id_inmuebles,
            "habitaciones"   : inmueble.balance,
            "banios"         : inmueble.banios,
            "alimentacion"   : inmueble.alimentacion,
            "valoracion"     : inmueble.valoracion,
            "precio"         : inmueble.precio,
            "descripcion"    : inmueble.descripcion,
            "ubicacion"      : inmueble.ubicacion,
            "lastChangeDate" : inmueble.lastChangeDate,
            "isAvailable"    : inmueble.isAvailable
        }