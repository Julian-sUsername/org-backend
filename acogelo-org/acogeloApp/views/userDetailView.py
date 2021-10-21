from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from acogeloApp.models.usuario import User
from acogeloApp.serializers.usuarioSerializer import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    #indican a la clase de Django REST, el modelo y el Serializer que debe utilizar dicha funcionalidad.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #indicarle a la clase de DjangoREST verificar que el usuario que hace la petición HTTP esté autenticado.
    permission_classes = (IsAuthenticated,)

    #tomar el id del usuario, y retornar su información solo si el access token es válido.
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        #Se compara que el usuario logueado tenga el mismo ID que del usuario del token 
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        return super().get(request, *args, **kwargs)