# plataforma/views.py

from django.shortcuts import render

# Definimos la función 'index'
def index(request):
    # Retornamos el renderizado de la plantilla 'inicio.html'
    return render(request, 'plataforma/index.html')

# Definimos la función 'perfil'
def perfil(request):
    # Retornamos el renderizado de la plantilla 'perfil.html'
    return render(request, 'plataforma/perfil.html')
