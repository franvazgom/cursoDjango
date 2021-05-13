from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        # Obtiene de la sesión el total
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields["total"].initial = total_float

    class Meta:
        model = Pedido
        fields = ['correo', 'nombre', 'direccion', 'colonia', 'total']
        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección, calle y número'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia o fraccionamiento'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
