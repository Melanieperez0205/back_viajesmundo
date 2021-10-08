from rest_framework                               import serializers
from authAppExample.models.user                   import User
from authAppExample.models.account                import Account
from authAppExample.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'account']
        
    def create(self, validated_data):
        accountData  = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user    = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id'      : user.id,
            'username': user.username,
            'email'   : user.email,
            'account' : {
                "id"             : account.id,
                "habitaciones"   : account.balance,
                "banios"         : account.banios,
                "alimentacion"   : account.alimentacion,
                "valoracion"     : account.valoracion,
                "precio"         : account.precio,
                "estado"         : account.estado,
                "descripcion"    : account.descripcion,
                "ubicacion"      : account.ubicacion,
                "lastChangeDate" : account.lastChangeDate
            }
        }