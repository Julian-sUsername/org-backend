# Generated by Django 3.2.8 on 2021-10-23 14:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombres', models.CharField(max_length=100, null=True)),
                ('apellidos', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('rol', models.CharField(max_length=1, null=True)),
                ('celular', models.BigIntegerField(null=True)),
                ('horario_contacto', models.CharField(max_length=50, null=True)),
                ('dpto_residencia', models.CharField(max_length=50, null=True)),
                ('ciudad_residencia', models.CharField(max_length=50, null=True)),
                ('aceptacion_termycond', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_masc', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_masc', models.CharField(max_length=50)),
                ('descripcion_larga_masc', models.TextField()),
                ('tipo_masc', models.CharField(max_length=20)),
                ('raza_masc', models.CharField(max_length=30)),
                ('edad_masc', models.CharField(max_length=30)),
                ('genero_masc', models.CharField(max_length=10)),
                ('dpto_residencia_masc', models.CharField(max_length=50)),
                ('ciudad_residencia_masc', models.CharField(max_length=50)),
                ('estado_adopcion_masc', models.CharField(max_length=15)),
                ('descripcion_foto_masc', models.CharField(max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dueno', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id_re', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_relacion', models.CharField(max_length=20)),
                ('estado_relacion', models.CharField(max_length=20)),
                ('id_masc_re', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acogeloApp.mascota')),
                ('id_user_re', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
