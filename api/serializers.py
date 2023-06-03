from rest_framework import serializers
from api.models import Paciente, Medico_Responsable, Tecnico_Responsable, Equipo
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class MedicoResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico_Responsable
        fields = '__all__'

class TecnicoResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico_Responsable
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'groups']
        extra_kwargs = {
            'password': {'write_only': True, 'requied': True}
        }
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user