from django.urls import path
from .views import PublicacionListCreateView, PublicacionDetailView,ComentarioViewSet

urlpatterns = [
    path('publicaciones/', PublicacionListCreateView.as_view(), name='publicacion-list'),
    path('publicaciones/<int:pk>/', PublicacionDetailView.as_view(), name='publicacion-detail'),
    path('comentarios/', ComentarioViewSet.as_view(), name='comentarios'),
]