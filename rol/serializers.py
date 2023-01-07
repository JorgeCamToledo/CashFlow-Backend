from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from rol.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('pk','id_user','rol')