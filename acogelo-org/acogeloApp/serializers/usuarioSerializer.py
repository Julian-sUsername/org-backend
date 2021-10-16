from rest_framework import serializers
from acogeloApp.models.usuario import User
from acogeloApp.models.mascota import Mascota
from acogeloApp.serializers.mascotaSerializer import MascotaSerializer

class UserSerializer(serializers.ModelSerializer):
    mascota = MascotaSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombres', 'apellidos', 'email', 'rol', 'celular', 'horario_contacto', 'dpto_residencia', 'ciudad_residencia', 'aceptacion_termycond', 'mascota']

    def create(self, validated_data):
        mascotaData = validated_data.pop('mascota')
        userInstance = User.objects.create(**validated_data)
        Mascota.objects.create(user=userInstance, **mascotaData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        mascota = Mascota.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'email': user.email,
            'mascota': {
                'id_masc': mascota.id_masc,
                'nombre_masc': mascota.nombre_masc,
                'descripcion_foto_masc': mascota.descripcion_foto_masc,
                'estado_adopcion_masc': mascota.estado_adopcion_masc
            }
        }       