from ast import Num
from django.db import models
from datetime import datetime, date
# Create your models here.

class tableIndi(models.Model):
    fecha= models.DateField(auto_now_add=True, unique=False)
    indicador=models.CharField(max_length=100, null=False)
    numSemana=models.IntegerField(null=False)
    semana1 =  models.IntegerField(default=0)
    semana2 = models.IntegerField(default=0)
    semana3 = models.IntegerField(default=0)
    semana4 = models.IntegerField(default=0)
    Razon=models.CharField(max_length=50, null=False, unique=True)
    monto=models.IntegerField(null=False)
    mes = models.CharField(max_length=50, null=False, default= datetime.today().month)
