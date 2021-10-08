from authAppExample.models.account     import Account
from authAppExample.models.transaction import Transaction
from rest_framework                    import serializers

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Transaction
        fields = ['inmueble_inicial', 'inmueble_final','register_date', 'note']
    
    def to_representation(self, obj):
        account_origin  = Account.objects.get(id=obj.inmueble_inicial_id)
        account_destiny = Account.objects.get(id=obj.inmueble_final_id)
        transaction     = Transaction.objects.get(id=obj.id)
        return {
            'id'            : transaction.id,
            'register_date' : transaction.register_date,
            'note'          : transaction.note,
            'origin_account' : {
                'id'            : account_origin.id,
                'habitaciones'  : account_origin.habitaciones,
                'banios'        : account_origin.banios,
                'alimentacion'  : account_origin.alimentacion,
                'valoracion'    : account_origin.valoracion,
                'precio'        : account_origin.precio,
                'estado'        : account_origin.estado,
                'descripcion'   : account_origin.descripcion,
                'ubicacion'     : account_origin.ubicacion
            },
            'destiny_account' : {
                'id'            : account_origin.id,
                'habitaciones'  : account_origin.habitaciones,
                'banios'        : account_origin.banios,
                'alimentacion'  : account_origin.alimentacion,
                'valoracion'    : account_origin.valoracion,
                'precio'        : account_origin.precio,
                'estado'        : account_origin.estado,
                'descripcion'   : account_origin.descripcion,
                'ubicacion'     : account_origin.ubicacion
            }
        }