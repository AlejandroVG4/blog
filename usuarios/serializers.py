from rest_framework import serializers
from .models import Comentario,Publicacion
from .models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ComentarioSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_hora', 'usuario_id', 'publicacion_id']

class PublicacionSerializer(serializers.ModelSerializer):
    # Aceptar la llave primaria  de los campos
    usuario_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(), write_only = True)
    class Meta:
        model = Publicacion
        fields = [
            'id',
            'fecha_hora',
            'usuario_id',
            'texto',
            'etiqueta'
        ]

class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()

        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
        except AuthenticationFailed:
            raise AuthenticationFailed("Username o password incorrecto")  
        return data
    
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class EliminarUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']  
        
class ActualizarPerfilSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ["username", "password"]

    def update(self, instance, validated_data):
        if "password" in validated_data:
            instance.set_password(validated_data["password"])  # Encripta la contraseña
        instance.username = validated_data.get("username", instance.username)
        instance.save()
        return instance
