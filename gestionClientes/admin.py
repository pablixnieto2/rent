from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'telefono']  # los campos que quieres mostrar en la lista
    search_fields = ['nombre', 'apellido']  # campos por los cuales puedes buscar
    list_filter = ['estado', 'como_nos_conocio']  # filtros que puedes aplicar en la barra lateral
   
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si es una creación y no una actualización de un objeto existente
            obj.creado_por = request.user
        super().save_model(request, obj, form, change)

    # Excluye el campo 'creado_por' del formulario
    exclude = ('creado_por',)