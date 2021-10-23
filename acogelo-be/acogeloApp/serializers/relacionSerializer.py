# -------------- SERIALIZER DE RELACION -------------------------

from acogeloApp.models.relacion import Relacion
from acogeloApp.models.mascota import Mascota
from acogeloApp.models.usuario import User
from rest_framework import serializers


class RelacionSerializer(serializers.ModelSerializer):
    class Meta:

        model = Relacion
        #        fields = ['mascota', 'usuario', 'tipo_relacion', 'estado_relacion']
        #fields = ['id_masc_re_id', 'id_user_re_id', 'tipo_relacion', 'estado_relacion']
        fields = ['id_masc_re', 'id_user_re', 'tipo_relacion', 'estado_relacion']
        
    def to_representation(self, obj):

        relation = Relacion.objects.get(id_re=obj.id_re)
        #relation = Relacion.objects.all()
        id_mascota = Mascota.objects.get(id_masc=obj.id_masc_re_id)
        #id_mascota = Mascota.objects.all()
        id_usuario = User.objects.get(id=obj.id_user_re_id)
        #id_usuario = User.objects.all()

        return {
        'id_re': relation.id_re,
        'tipo_relacion': relation.tipo_relacion,
        'estado_relacion': relation.estado_relacion,
        'id_masc_re_id': {
            'id_masc': id_mascota.id_masc,
            'nombre_masc': id_mascota.nombre_masc,
            'descripcion_larga_masc': id_mascota.descripcion_larga_masc,
            'tipo_masc': id_mascota.tipo_masc,
            'raza_masc': id_mascota.raza_masc,
            'edad_masc': id_mascota.edad_masc,
            'genero_masc': id_mascota.genero_masc,
            'dpto_residencia_masc': id_mascota.dpto_residencia_masc,
            'ciudad_residencia_masc': id_mascota.ciudad_residencia_masc,
            'estado_adopcion_masc': id_mascota.estado_adopcion_masc,
            'descripcion_foto_masc': id_mascota.descripcion_foto_masc},
        'id_user_re_id': {
            'id': id_usuario.id,
            'username': id_usuario.username,
            'nombres': id_usuario.nombres,
            'apellidos': id_usuario.apellidos,
            'email': id_usuario.email,
            'rol': id_usuario.rol,
            'celular': id_usuario.celular,
            'horario_contacto': id_usuario.horario_contacto,
            'dpto_residencia': id_usuario.dpto_residencia,
            'ciudad_residencia': id_usuario.ciudad_residencia,
            'aceptacion_termycond': id_usuario.aceptacion_termycond}}