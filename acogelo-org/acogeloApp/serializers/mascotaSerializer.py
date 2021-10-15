from acogeloApp.models.mascota import Mascota
from rest_framework import serializers

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        #fields = ['balance', 'lastChangeDate', 'isActive']
        fields = ['nombre_masc', 'descripcion_larga_masc', 'tipo_masc', 'raza_masc', 'edad_masc', 'genero_masc', 'dpto_residencia_masc', 'ciudad_residencia_masc', 'estado_adopcion_masc', 'ruta_foto_masc', 'descripcion_foto_masc']

        """
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
    

    id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
	balance = models.IntegerField(default=0)
	lastChangeDate = models.DateTimeField()
	isActive = models.BooleanField(default=True)
    """
