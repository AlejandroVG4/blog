from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Publicacion
from .serializers import PublicacionSerializer


# Create your views here.
class registro(generics.ListCreateAPIView):
     pass

class PublicacionListCreateView(generics.ListCreateAPIView):
     permission_classes = [permissions.AllowAny]
     queryset = Publicacion.objects.all()
     serializer_class = PublicacionSerializer

     def perform_create(self, serializer):
          serializer.save(usuario_id=self.request.user)

class PublicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
     queryset = Publicacion.objects.all()
     serializer_class = PublicacionSerializer
     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

     def perform_update(self, serializer):
        serializer.save(autor=self.request.user)