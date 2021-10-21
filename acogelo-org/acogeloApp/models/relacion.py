from django.db import models
from .mascota import Mascota
from .usuario import User

class Mascota(models.Model):
    id_masc = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE)    
    id_user = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    tipo_relacion = models.CharField(max_length = 20, unique=False)
    estado_relacion = models.CharField(max_length = 20, unique=False)