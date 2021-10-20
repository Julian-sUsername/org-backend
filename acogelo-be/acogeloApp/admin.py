from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models.usuario import User
from .models.mascota import Mascota
admin.site.register(User)
admin.site.register(Mascota)