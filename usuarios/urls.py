from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    path('eliminar/', views.EliminarUsuarioView.as_view(), name='eliminar_usuario'),
    path('actualizar/', views.ActualizarPerfilView.as_view(), name='actualizar')
]

