from django import forms
from .models import Account


class InmuebleForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('habitaciones', 'banios', 'alimentacion','valoracion','precio','descripcion','ubicacion','lastChangeDate','isAvailable')
