from django.db import models
from .mascota import Mascota
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length = 15, unique=True)
    password = models.CharField(max_length = 256)
    nombres = models.CharField(max_length = 100, unique=False, null=True)
    apellidos= models.CharField(max_length = 100, unique=False, null=True)
    email = models.EmailField(max_length = 100)
    rol = models.CharField(max_length = 1, unique=False, null=True)
    celular = models.BigIntegerField(null=True)
    horario_contacto = models.CharField(max_length = 50, unique=False, null=True)
    dpto_residencia = models.CharField(max_length = 50, unique=False, null=True)
    ciudad_residencia = models.CharField(max_length = 50, unique=False, null=True)
    aceptacion_termycond = models.BooleanField(default=False, unique=False)
    id_masc = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE, null=True)