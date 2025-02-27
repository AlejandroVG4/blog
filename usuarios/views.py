from rest_framework import generics
from .models import Publicacion
from .serializers import PublicacionSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comentario
from .serializers import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
     queryset = Comentario.objects.all()
     serializer_class = ComentarioSerializer
     permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

     def perform_create(self, serializer):
          """
          Asigna automáticamente el usuario logueado al comentario.
          """
          serializer.save(usuario=self.request.user)

class PublicacionListCreateView(generics.ListCreateAPIView):
     permission_classes = [AllowAny]
     queryset = Publicacion.objects.all()
     serializer_class = PublicacionSerializer

     def perform_create(self, serializer):
          serializer.save(usuario_id=self.request.user)

class PublicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Publicacion.objects.all()
     serializer_class = PublicacionSerializer
     permission_classes = [IsAuthenticated]

     def perform_update(self, serializer):
        serializer.save(autor=self.request.user)