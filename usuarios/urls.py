from django.urls import path
from .views import PublicacionListCreateView, PublicacionDetailView

urlpatterns = [
    path('publicaciones/', PublicacionListCreateView.as_view(), name='publicacion-list'),
    path('publicaciones/<int:pk>/', PublicacionDetailView.as_view(), name='publicacion-detail'),
]