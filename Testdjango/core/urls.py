from django.urls import path
from core.views import home,agregar_proveedores, proveedores,eliminar_proveedores,modificar_proveedores,mensaje_modificar

app_name='core'

urlpatterns = [
    path('home/', home, name="home"),
    path('agregar/', agregar_proveedores , name="agregar"),
    path('proveedores/', proveedores , name="proveedores"),
    path('eliminar/<id>', eliminar_proveedores , name="eliminar"),
    path('modificar/<id>', modificar_proveedores , name="modificar"),
    path('mensaje/', mensaje_modificar, name="mensaje"),

]