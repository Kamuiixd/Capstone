# plataforma/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Llamamos a la función 'inicio' desde 'views'
    path('perfil/', views.perfil, name='perfil'),  # Llamamos a la función 'perfil' desde 'views'
]
