from dataclasses import fields
from rest_framework import routers, serializers, viewsets

#importacion do modelos

from Flujo.models import FlujoEfec
from categorias.models import Categoria

class FlujoEfecSerializer(serializers.ModelSerializer):
    categoria = serializers.ReadOnlyField(source = 'id_categoria.categoria')
    subCategoria = serializers.ReadOnlyField(source = 'id_categoria.subCategoria')
    class Meta:
        model = FlujoEfec
        fields = ('pk','fecha','mes','descripcion','tipo_flujo','id_categoria', 'cantidad','categoria','subCategoria')
