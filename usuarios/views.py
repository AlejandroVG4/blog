from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.permissions import AllowAny, IsAuthenticated 
from .models import User
from .serializers import RegistroSerializer, PerfilSerializer, EliminarUsuarioSerializer, ActualizarPerfilSerializer

# Create your views here.
class RegistroView(generics.CreateAPIView):
     permission_classes = [AllowAny]
     queryset = User.objects.all()
     serializer_class = RegistroSerializer

class PerfilView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PerfilSerializer
   
    def get_object(self):
        return self.request.user

class EliminarUsuarioView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = EliminarUsuarioSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user 
   
    def delete(self, request, *args, **kwargs):
         
        usuario = self.get_object()
        usuario.delete()
        return response.Response(
            {"message": "Tu cuenta ha sido eliminada correctamente."},
            status=status.HTTP_200_OK
        )

class ActualizarPerfilView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActualizarPerfilSerializer

    def get_object(self):
        return self.request.user  # Obtiene el usuario autenticado

    def update(self, request, *args, **kwargs):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            {"message": "Perfil actualizado correctamente.", "data": serializer.data},
            status=status.HTTP_200_OK
        )