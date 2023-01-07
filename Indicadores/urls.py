from django.urls import path, re_path
from django.conf.urls import include

# Importacion de la vista
from Indicadores.views import IndicadorFechaBanco, IndicadorFechaCobrar, IndicadorFechaPagar, indicadoresList, indicadoresDetail

urlpatterns = [
    re_path(r'^indicadores/$', indicadoresList.as_view()),
    re_path(r'^indicadores/(?P<pk>\d+)$', indicadoresDetail.as_view()),
    re_path(r'^indicobrar/(?P<pk>\d+)$', IndicadorFechaCobrar.as_view()),
    re_path(r'^indipagar/(?P<pk>\d+)$', IndicadorFechaPagar.as_view()),
    re_path(r'^indibanco/(?P<pk>\d+)$', IndicadorFechaBanco.as_view()),
]