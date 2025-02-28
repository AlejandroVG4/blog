from rest_framework import generics
from .models import Publicacion
from .serializers import PublicacionSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comentario
from .serializers import ComentarioSerializer
from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated 
from .models import User
from .serializers import RegistroSerializer, PerfilSerializer, EliminarUsuarioSerializer, ActualizarPerfilSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class ComentarioViewSet(generics.ListCreateAPIView):
     queryset = Comentario.objects.all()
     serializer_class = ComentarioSerializer
     permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

     def perform_create(self, serializer):
          """
          Asigna automáticamente el usuario logueado al comentario.
          """
          serializer.save(usuario=self.request.user)

class PublicacionCreateView(APIView):
     permission_classes = [IsAuthenticated]
     
     def post(self, request):
         
         #Extraer los datos de la request
        texto = request.data.get('texto')
        etiqueta = request.data.get('etiqueta')
        usuario= User.objects.get(id=request.user.id)
        usuario_id = usuario.id

        print(usuario_id)

        publicacion_data = {
            "texto" : texto,
            "etiqueta" : etiqueta,
            "usuario_id" : usuario_id
        }

        serializer = PublicacionSerializer(data=publicacion_data)
        if serializer.is_valid():
            serializer.save()
            publicacion = serializer.data
            return Response({"mensaje" : "Publicacion creada con exito", "publicacion" : publicacion}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicacionListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

    def get_queryset(self):
        user = self.request.user
        return Publicacion.objects.filter(usuario_id=user)

class PublicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Publicacion.objects.all()
     serializer_class = PublicacionSerializer
     permission_classes = [IsAuthenticated]

     def perform_update(self, serializer):
        serializer.save(autor=self.request.user)


# Create your views here.
class RegistroView(generics.CreateAPIView):
     permission_classes = [AllowAny]
     queryset = User.objects.all()
     serializer_class = RegistroSerializer
     
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class PerfilView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PerfilSerializer
   
    def get_object(self):
        return self.request.user

class EliminarUsuarioView(generics.DestroyAPIView):
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
        return self.request.user

    def update(self, request, *args, **kwargs):
        usuario = self.get_object()
        serializer = self.get_serializer(usuario, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            {"message": "Perfil actualizado correctamente.", "data": serializer.data},
            status=status.HTTP_200_OK
        )
