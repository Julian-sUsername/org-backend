from rest_framework import serializers
from acogeloApp.models.usuario import User
from acogeloApp.models.mascota import Mascota
from acogeloApp.serializers.mascotaSerializer import MascotaSerializer

class UserSerializer(serializers.ModelSerializer):
    mascota = MascotaSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'nombres', 'apellidos', 'email', 'rol', 'celular', 'horario_contacto', 'dpto_residencia', 'ciudad_residencia', 'aceptacion_termycond', 'mascota']

    """
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombres = models.CharField(max_length = 100, unique=False, null=True)
    apellidos= models.CharField(max_length = 100, unique=False, null=True)
    email = models.EmailField('Email', max_length = 100)
    rol = models.CharField(max_length = 1, unique=False, null=True)
    celular = models.BigIntegerField(null=True)
    horario_contacto = models.CharField(max_length = 50, unique=False, null=True)
    dpto_residencia = models.CharField(max_length = 50, unique=False, null=True)
    ciudad_residencia = models.CharField(max_length = 50, unique=False, null=True)
    aceptacion_termycond = models.BooleanField(default=False, unique=False)
    id_masc = models.ForeignKey(Mascota, related_name='mascota', on_delete=models.CASCADE, default=0)
    """

    def create(self, validated_data):
        accountData = validated_data.pop('mascota')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance
    
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        mascota = Account.objects.get(user=obj.id)
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