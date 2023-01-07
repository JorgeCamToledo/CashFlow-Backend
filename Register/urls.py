from django.urls import path, re_path
from django.conf.urls import include


# Importacion de la vista
from Register.views import RegistroView

urlpatterns = [
    re_path(r'^register/$', RegistroView.as_view())
]
