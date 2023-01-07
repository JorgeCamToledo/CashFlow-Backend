from email.policy import default
from django.db import models

class Categoria(models.Model):
    subCategoria= models.CharField(max_length=50, null=False)
    categoria = models.CharField(max_length=50, null=False)
    tipo = models.CharField(max_length=50, null=False, default="")



    class Meta:
        managed: True
        db_table: 'Categoria'


# Create your models here.
