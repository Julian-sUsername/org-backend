from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from acogeloApp.serializers.usuarioSerializer import UserSerializer
from acogeloApp.serializers.mascotaSerializer import MascotaSerializer
from acogeloApp.serializers.relacionSerializer import RelacionSerializer


from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from django.conf import settings

from acogeloApp.models.usuario import User
from acogeloApp.models.mascota import Mascota
from acogeloApp.models.relacion import Relacion

#definicion de la clase UserCreateView (que abstrae de APIView)
# =================================== CREAR USUARIO ===================================
class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"username":request.data["username"],
                     "password":request.data["password"]}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

# =================================== TRAER UN USUARIO ===================================
class UserDetailView(generics.RetrieveAPIView):
    #indican a la clase de Django REST, el modelo y el Serializer que debe utilizar dicha funcionalidad.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #indicarle a la clase de DjangoREST verificar que el usuario que hace la petición HTTP esté autenticado.
    permission_classes = (IsAuthenticated,)

    #tomar el id del usuario, y retornar su información solo si el access token es válido.
    def get(self, request, *args, **kwargs):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        #Se compara que el usuario logueado tenga el mismo ID que del usuario del token
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)


# =================================== VER MASCOTAS EN ADOPCION ===================================
# OK - MascotaDetailView PARA CONSULTAR *1* DE *MIS* MASCOTAS QUE QUIERO ADOPTAR	
# #path('misMascotas/adoptar/<int:id_user_re>/<int:id_masc_re>/', views.MascotasDetailView.as_view()),

class MascotaDetailView(generics.RetrieveAPIView):
    queryset = Relacion.objects.all()
    serializer_class = RelacionSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['id_user_re_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        try:
            queryset = Relacion.objects.get(id_user_re_id=self.kwargs['id_user_re_id'], id_masc_re_id=self.kwargs['id_masc_re_id'], estado_relacion__contains = 'activa', tipo_relacion__contains=self.kwargs['pk'])
            #print(queryset)
            #print(Response(RelacionSerializer(queryset).data))
            #return queryset
            #return Response(queryset, status=status.HTTP_200_OK)
            return Response(RelacionSerializer(queryset).data)
            #return Response(queryset)

        except Exception as e:
            print(e)
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

# =================================== CREAR MASCOTA ===================================
class MascotasCreateView(generics.CreateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
    
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        #Se compara que el usuario logueado tenga el mismo ID que del usuario del token
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = MascotaSerializer(data=request.data)
        # Verificar que coincida con los tipos de datos en el modelo
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'detail': 'Mascota añadida exitosamente'}, status=status.HTTP_201_CREATED)

# OK - MascotasView PARA CONSULTAR LISTA DE *TODAS* LAS MASCOTAS DISPONIBLES PARA ADOPTAR 
#    path('getMascotas/<int:pk>/', views.MascotasView.as_view()),
# =================================== TRAER LISTA DE MASCOTAS ===================================
class MascotasView(generics.ListAPIView):
    serializer_class = MascotaSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)
        
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        try:
            queryset = Mascota.objects.filter(estado_adopcion_masc__contains = 'En adopción')
            return queryset

        except Exception as e:
            print(e)
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

# OK - MascotasDetailView PARA CONSULTAR LISTA DE *TODAS* *MIS* MASCOTAS DISPONIBLES PARA ADOPTAR 
#    path('misMascotas/adoptar/<int:id_user_re>/<str:pk>/', views.MascotasDetailView.as_view()),
# =================================== TRAER LISTA DE MASCOTAS ===================================
class MascotasDetailView(generics.ListAPIView):
    serializer_class = RelacionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)
        
        token = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != self.kwargs['id_user_re_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        try:
            queryset = Relacion.objects.filter(estado_relacion__contains = 'activa', tipo_relacion__contains=self.kwargs['pk'], id_user_re_id=self.kwargs['id_user_re_id'])
            return queryset

        except Exception as e:
            print(e)
            return Response({'detail': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)

# =================================== UPDATE MASCOTA ===================================
class MascotaUpdateView(generics.UpdateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        #if valid_data['user_id'] != kwargs['pk']:
        if valid_data['user_id'] != kwargs['user_id_id']:       
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().update(request, *args, **kwargs)

# OK - MascotaDeleteView PARA ELIMINAR *1* DE *MIS* MASCOTAS QUE PUSE EN ADOPCIÓN	
#    path('misMascotas/eliminar/<int:user_id_id>/<int:pk>/', views.MascotaDeleteView.as_view()),
# =================================== VER MASCOTA ===================================
class MascotaDeleteView(generics.DestroyAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)
        
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        #if valid_data['user_id'] != kwargs['id_user_re']:
        if valid_data['user_id'] != kwargs['user_id_id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().destroy(request, *args, **kwargs)

# =================================== CREAR RELACION ===================================
class RelacionCreateView(generics.CreateAPIView):
    queryset = Relacion.objects.all()
    serializer_class = RelacionSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        print("request:",self.request)
        print("args:",self.args)
        print("kwargs:",self.kwargs)

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        serializer = RelacionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'detail': 'Gracias por iniciar el proceso de adopción'}, status=status.HTTP_201_CREATED)