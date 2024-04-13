from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ClienteForm
from .models import Cliente

def registro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_clientes'))
    else:
        form = ClienteForm(user=request.user)
    return render(request, 'gestionClientes/registro_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestionClientes/lista_clientes.html', {'clientes': clientes})
