from acogeloApp.models.relacion import Relacion
from rest_framework import serializers

class RelacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relacion
        fields = ['mascota', 'usuario', 'tipo_relacion', 'estado_relacion']