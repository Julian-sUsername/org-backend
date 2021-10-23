"""acogeloProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from acogeloApp import views

urlpatterns = [
    #Register to the site for the first time
    path('user/', views.UserCreateView.as_view()),  
    
    #Login using username and password
    path('login/', TokenObtainPairView.as_view()),

    #Refresh access Token
    # --- Ejemplo: Para renovar el access token, se pone POST + Access Token viejo + Json con el Request token + http:xxx/refresh
    path('refresh/', TokenRefreshView.as_view()),

    #Get my personal info
    # --- Ejemplo: Para conocer mi información personal, se pone GET + Access Token + http:xxx/user/1, donde 1 es el id de mi usuario de login
    path('user/<int:pk>/', views.UserDetailView.as_view()),

    #Post a pet
    # --- Ejemplo: Para crear una mascota se pone POST + Access Token + Json + http:xxx/mascotas/1/, donde 1 es el id de mi usuario de login
    path('mascotas/<int:pk>/', views.MascotasCreateView.as_view()),

    #Post a relation
    # --- Ejemplo: Para crear una relación se pone POST + Access Token + Json + http:xxx/relacion/1/, donde 1 es el id de mi usuario de login
    path('relacion/<int:pk>/', views.RelacionCreateView.as_view()),

    #Get a pet
    # --- Ejemplo: Para consultar una sola mascota en la que estoy interesado en adoptar, se pone:
    # GET + Access Token + http:xxx/misMascotas/adoptar/1/interesado/2/, , donde 1 es el id de mi usuario de login y 2 es el id de la mascota
    path('misMascotas/adoptar/<int:id_user_re_id>/<str:pk>/<int:id_masc_re_id>/', views.MascotaDetailView.as_view()),

    #Get a pet list
    # --- Ejemplo: Para consultar todas las mascotas en las que estoy interesado en adoptar, se pone:
    # GET + Access Token + http:xxx/misMascotas/adoptar/1/interesado, , donde 1 es el id de mi usuario de login
    path('misMascotas/adoptar/<int:id_user_re_id>/<str:pk>/', views.MascotasDetailView.as_view()),

    #Get All
    # --- Ejemplo: Para consultar todas las mascotas disponibles para adoptar, se pone:
    # GET + Access Token + http:xxx/getMascotas/1/, , donde 1 es el id de mi usuario de login
    path('getMascotas/<int:pk>/', views.MascotasView.as_view()),

    #Update pet
    # --- Ejemplo: Para actualizar la información de una mascota, se pone:
    # GET + Access Token + Json con toda la info + http:xxx/updateMascotas/1/2/, donde 1 es el id de mi usuario de login y 2 es el id de la mascota a actualizar
    #path('updateMascotas/<int:pk>/', views.MascotaUpdateView.as_view()), --> esta no funcionó
    path('updateMascotas/<int:user_id_id>/<int:pk>/', views.MascotaUpdateView.as_view()),

    #Delete pet
    # --- Ejemplo: Para eliminar la información de una mascota, se pone:
    # GET + Access Token + http:xxx/misMascotas/eliminar/1/2/, donde 1 es el id de mi usuario de login y 2 es el id de la mascota a eliminar
    path('misMascotas/eliminar/<int:user_id_id>/<int:pk>/', views.MascotaDeleteView.as_view()),
]