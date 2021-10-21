from django.db import models

class Mascota(models.Model):

    id_masc = models.AutoField(primary_key=True, default=0)
    nombre_masc = models.CharField(max_length = 50, unique=False)
    descripcion_larga_masc = models.TextField()
    tipo_masc = models.CharField(max_length = 20, unique=False)
    raza_masc = models.CharField(max_length = 30, unique=False)
    edad_masc = models.CharField(max_length = 30, unique=False)
    genero_masc = models.CharField(max_length = 10, unique=False)
    dpto_residencia_masc = models.CharField(max_length = 50, unique=False)
    ciudad_residencia_masc = models.CharField(max_length = 50, unique=False)
    estado_adopcion_masc = models.CharField(max_length = 15, unique=False)
    ruta_foto_masc = models.ImageField(max_length = 200, unique=False)
    descripcion_foto_masc = models.CharField(max_length = 50, unique=False)