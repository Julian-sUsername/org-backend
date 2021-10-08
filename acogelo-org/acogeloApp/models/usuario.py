from django.db import models
from .mascota import Mascota
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length = 15, unique=True)
    password = models.CharField('Password', max_length = 256)
    nombres: models.CharField(max_length = 100, unique=False)
    apellidos: models.CharField(max_length = 100, unique=False)
    email = models.EmailField('Email', max_length = 100)
    rol: models.CharField(max_length = 1, unique=False)
    celular: models.BigIntegerField()
    horario_contacto: models.CharField(max_length = 50, unique=False)
    dpto_residencia: models.CharField(max_length = 50, unique=False)
    ciudad_residencia: models.CharField(max_length = 50, unique=False)
    aceptacion_termycond: models.BooleanField(default=False, unique=False)
    id_masc_usuario: models.ForeignKey(Mascota, related_name='mascotas', on_delete=models.CASCADE)
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'