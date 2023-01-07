from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id_user = models.OneToOneField(User,on_delete=models.CASCADE)
    rol = models.CharField(max_length=20,null=False)
