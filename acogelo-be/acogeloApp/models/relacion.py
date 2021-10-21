from django.db import models
from .mascota import Mascota
from .usuario import User

class Relacion(models.Model):
    id_masc = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE)    
    id_user = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    # Dueño o interesado
    tipo_relacion = models.CharField(max_length = 20, unique=False)
    # Adoptado o en adopcion
    estado_relacion = models.CharField(max_length = 20, unique=False)