from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from categorias.models import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('pk','subCategoria','categoria', 'tipo',)