from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('test-firestore-connection/', views.test_firestore_connection, name='test_firestore_connection'),  # Asegúrate de que esta línea esté presente
]

