from rest_framework import serializers
from .models import Comentario,Publicacion

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'fecha_hora', 'usuario', 'publicacion']

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
