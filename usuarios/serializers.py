from rest_framework import serializers
from .models import Comentario,Publicacion
from .models import User

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_hora', 'usuario_id', 'publicacion_id']

    def create(self, validated_data):
        """
        Asigna el usuario logueado automáticamente al comentario cuando se crea.
        """
        user = self.context['request'].user
        return Comentario.objects.create(usuario=user, **validated_data)

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = '__all__'


class RegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Extraemos la contraseña de validated_data
        password = validated_data.pop('password')

        # Creamos el usuario utilizando serializer.save() y pasamos los datos validados
        user = super().create(validated_data)

        # Encriptamos la contraseña usando set_password
        user.set_password(password)

        # Guardamos el usuario en la base de datos
        user.save()

        return user
    
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
