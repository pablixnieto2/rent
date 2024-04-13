from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # Ajustes adicionales, por ejemplo, establecer un usuario por defecto
        if user is not None:
            self.fields['creado_por'].initial = user
