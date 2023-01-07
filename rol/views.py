from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path
from django.contrib.auth.models import User

#Importaciones de modelos
from rol.models import Usuario

#Importaciones de serializadores
from rol.serializers import UsuarioSerializer

# Create your views here.
class RolList(APIView):
    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404
    
    def get(self,request,format=None):
        queryset=Usuario.objects.all()
        serializer = UsuarioSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request):
        #archivos = request.data['url_image']
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            rol = Usuario(**validated_data)
            rol.save()
            serializer_response = UsuarioSerializer(rol)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response("Este usuario ya tiene un perfil")

class RolDetail(APIView):
    def get_object(self, pk):
        try:
            return Usuario.objects.get(id_user = pk)
        except Usuario.DoesNotExist:
            return 404
    def res_custom(self, user, data, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "id_user" : data.get('id_user'),
            "rol" : data.get('rol'),
            "status" : status
        }
        return response;

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = UsuarioSerializer(idResponse)
            user = User.objects.filter(id=pk).values()
            responseOK = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
