from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import exceptions
import os.path
from pathlib import Path
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# importaciones de modelos agregados
from categorias.models import Categoria 

# importaciones de serializadores
from categorias.serializers import CategoriaSerializer

# Create your views here.

        

class CategoriaList(APIView):
    def get(self, request, format=None):
        queryset = Categoria.objects.all()
        serializer = CategoriaSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            categoria = Categoria(**validated_data)
            categoria.save()
            serializer_response = CategoriaSerializer(categoria)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class CategoriaDetail(APIView):
     def get_object(self, pk):
         try:
             return Categoria.objects.get(pk = pk)
         except Categoria.DoesNotExist:
             return 0

     def get(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         if idResponse != 0:
             idResponse = CategoriaSerializer(idResponse)
             return Response(idResponse.data, status = status.HTTP_200_OK)
         return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

     def put(self, request,pk, format=None):
         idResponse = self.get_object(pk)
         serializer = CategoriaSerializer(idResponse, data = request.data)
         if serializer.is_valid():
             serializer.save()
             datas = serializer.data
             return Response(datas, status = status.HTTP_201_CREATED)
         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


     def delete(self, request, pk):
         categoria = self.get_object(pk)
         if categoria != 0:
             categoria.delete()
             return Response("Dato eliminado",status=status.HTTP_204_NO_CONTENT)
         return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST) 

class CategoriaEntrada(generics.ListAPIView):
    def get(self, request, format=None):
        queryset = Categoria.objects.filter(tipo = "Entrada")
        serializer = CategoriaSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoriaSalida(generics.ListAPIView):
    def get(self, request, format=None):
        queryset = Categoria.objects.filter(tipo="Salida")
        serializer = CategoriaSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
