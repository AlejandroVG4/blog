from django.shortcuts import render
from rest_framework import generics

# blog/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Comentario
from .Serializer import ComentarioSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
     queryset = Comentario.objects.all()
     serializer_class = ComentarioSerializer
     permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

     def perform_create(self, serializer):
          """
          Asigna automáticamente el usuario logueado al comentario.
          """
          serializer.save(usuario=self.request.user)
