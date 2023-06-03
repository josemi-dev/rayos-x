from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from api.models import Paciente, Medico_Responsable, Tecnico_Responsable, Equipo
from api.serializers import PacienteSerializer, MedicoResponsableSerializer, TecnicoResponsableSerializer, EquipoSerializer, UserSerializer
from rest_framework import status, views, response
from rest_framework import authentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [permissions.AllowAny]

class Medico_ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Medico_Responsable.objects.all()
    serializer_class = MedicoResponsableSerializer
    permission_classes = [permissions.AllowAny]

class Tecnico_ResponsableViewSet(viewsets.ModelViewSet):
    queryset = Tecnico_Responsable.objects.all()
    serializer_class = TecnicoResponsableSerializer
    permission_classes = [permissions.AllowAny]

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [permissions.AllowAny]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser,]
    authentication_classes = [authentication.BasicAuthentication,]

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        # Recuperamos las credenciales y autenticamos al usuario
        username2= request.data.get('username', None)
        password2 = request.data.get('password', None)
        if username2 is None or password2 is None:
            return response.Response({'message': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        user2 = authenticate(username=username2, password=password2)
        if not user2:
            return response.Response({'message': 'Usuario o Contraseña incorrecto !!!! '},status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user2)
        # Si es correcto añadimos a la request la información de sesión
        if user2:
            # para loguearse una sola vez
            # login(request, user)
            return response.Response({'message':'usuario y contraseña correctos!!!!'},status=status.HTTP_200_OK)
            #return response.Response({'token': token.key}, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return response.Response(status=status.HTTP_404_NOT_FOUND)        

class LogoutView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self, request):        
        request.user.auth_token.delete()
        # Borramos de la request la información de sesión
        logout(request)
        # Devolvemos la respuesta al cliente
        return response.Response({'message':'Sessión Cerrada y Token Eliminado !!!!'},status=status.HTTP_200_OK)