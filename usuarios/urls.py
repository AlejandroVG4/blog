from django.urls import path
from .views import PublicacionCreateView, PublicacionDetailView,ComentarioViewSet, PublicacionListView, ComentarioListView
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    path('eliminar/', views.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('actualizar/', views.ActualizarPerfilView.as_view(), name='actualizar'),
    path('publicaciones/', PublicacionListView.as_view(), name='publicacion-list'),
    path('publicaciones/crear/', PublicacionCreateView.as_view(), name='publicacion-list'),
    path('publicaciones/<int:pk>/', PublicacionDetailView.as_view(), name='publicacion-detail'),
    path('comentarios/', ComentarioListView.as_view(), name='comentarios'),
    path('comentarios/crear/', ComentarioViewSet.as_view(), name='comentarios'),
]