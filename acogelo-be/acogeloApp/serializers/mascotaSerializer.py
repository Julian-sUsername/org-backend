from acogeloApp.models.mascota import Mascota
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        # fields = ['nombre_masc', 'descripcion_larga_masc', 'tipo_masc', 'raza_masc', 'edad_masc', 'genero_masc', 'dpto_residencia_masc', 'ciudad_residencia_masc', 'estado_adopcion_masc', 'descripcion_foto_masc']
        fields = ['id_masc','nombre_masc', 'descripcion_larga_masc', 'tipo_masc', 'raza_masc', 'edad_masc', 'genero_masc', 'dpto_residencia_masc', 'ciudad_residencia_masc', 'estado_adopcion_masc', 'descripcion_foto_masc', 'user_id']