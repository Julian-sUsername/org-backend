from rest_framework import serializers
from django.db import models
#from acogeloApp.models.usuario import User
from acogeloApp.models.mascota import Mascota
from acogeloApp.serializers.mascotaSerializer import MascotaSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'nombres', 'apellidos','rol', 'celular', 'horario_contacto', 'dpto_residencia', 'ciudad_residencia', 'aceptacion_termycond', 'mascota']