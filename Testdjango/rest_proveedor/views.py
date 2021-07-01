from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Proveedor 
from .serializers import ProveedorSerializer
@csrf_exempt
@api_view(['GET'])
def lista_proveedores(request):
    """
    Lista todos los Proveedores
    """
    proveedor = Proveedor.objects.all()
    serializer = ProveedorSerializer(proveedor, many=True)
    return Response(serializer.data)


# Create your views here.
