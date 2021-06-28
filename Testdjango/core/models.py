from django.db import models

# Create your models here.

class Proveedor(models.Model):
    rut=models.CharField(max_length=20)
    razon_social=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    servicio=models.CharField(max_length=50)
  
    def str(self):
        return self.rut