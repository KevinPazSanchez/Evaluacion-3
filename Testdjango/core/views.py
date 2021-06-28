from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProveedorForm
from .models import Proveedor

# Create your views here.

def home(request):

    return render(request, 'core/home.html')


def agregar_proveedores(request):

    data = {
        'form': ProveedorForm()
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Proveedor agregado exitosamente"
        else:
            data["form"] = formulario
    
    return render(request, 'core/agregar_proveedores.html',data)

def proveedores(request):

    proveedores = Proveedor.objects.all()
    data = {
        'proveedores': proveedores
    }
    
    return render(request, 'core/proveedores.html', data)


def eliminar_proveedores(request,id):

    proveedores = get_object_or_404(Proveedor, id=id)
    proveedores.delete()
    return redirect(to='core:proveedores')   

def modificar_proveedores(request,id):

    proveedores = get_object_or_404(Proveedor, id=id)
    data = {
        'form': ProveedorForm(instance=proveedores)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedores)
        if formulario.is_valid():             
            formulario.save()            
            return redirect(to='core:mensaje')
        data["form"] = formulario
    return render(request, 'core/modificar_proveedor.html', data)

def mensaje_modificar(request):

    return render(request, 'core/mensaje_modificar.html',{})
   