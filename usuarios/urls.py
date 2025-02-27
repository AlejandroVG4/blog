# blog/urls.py

from django.urls import path, include
from .views import ComentarioViewSet


urlpatterns = [
path('comentarios/', ComentarioViewSet.as_view(), name='comentarios'),
]