from django.urls import path 
from rest_proveedor.views import lista_proveedores, agregar_proveedor

urlpatterns = [
    path('lista_proveedores', lista_proveedores, name='lista_proveedores'),
    path('agregar_proveedor', agregar_proveedor, name='agregar_proveedor' ),
]