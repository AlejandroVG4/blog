from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Publicacion(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)  
    texto = models.TextField()
    etiqueta = models.ForeignKey(Etiqueta, on_delete=models.CASCADE)  

    def __str__(self):
        return f"Publicación de {self.usuario.username} - {self.texto[:20]}..." 

class Comentario(models.Model):
    fecha_hora = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    publicacion_id = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)

