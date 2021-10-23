from django.db import models
from .mascota import Mascota
from .usuario import User

class Relacion(models.Model):
    id_re = models.AutoField(primary_key=True)
    id_masc_re = models.ForeignKey(Mascota, on_delete=models.CASCADE)    
    id_user_re = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    # Dueño o interesado
    tipo_relacion = models.CharField(max_length = 20, unique=False)
    # Activo o inactivo
    estado_relacion = models.CharField(max_length = 20, unique=False)