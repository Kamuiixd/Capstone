# plataforma/views.py

from firebase_admin import auth
from django.shortcuts import render, redirect
from django.contrib import messages

# Definimos la función 'index'
def index(request):
    # Retornamos el renderizado de la plantilla 'inicio.html'
    return render(request, 'plataforma/index.html')

# Definimos la función 'perfil'
def perfil(request):
    # Retornamos el renderizado de la plantilla 'perfil.html'
    return render(request, 'plataforma/perfil.html')

# Definimos la Funcion Guardado de registro
def register_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Crear usuario en Firebase Authentication
            user = auth.create_user(email=email, password=password)
            # Aquí puedes añadir lógica adicional para guardar otros detalles en Firestore
            # o en tu base de datos en Django.

            return redirect('login')  # Redirige al inicio de sesión después de registrarse
        except Exception as e:
            return render(request, 'registro.html', {'error': str(e)})
    
    return render(request, 'registro.html')

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Firebase Authentication para verificar el usuario
            user = auth.get_user_by_email(email)
            # Guardar el UID del usuario en la sesión
            request.session['user'] = user.uid  

            # Aquí puedes implementar la verificación de contraseña y otros detalles de seguridad
            # Firebase Admin no gestiona la verificación de contraseña, pero puedes usar otras técnicas
            # o crear un servicio externo para ello.

            # Luego de verificar al usuario, puedes iniciar una sesión en Django
            request.session['user'] = user.uid  # Guardar el UID del usuario en la sesión
            return redirect('index')  # Redirige a la página de inicio
        except Exception as e:
            messages.error(request, "Credenciales inválidas o usuario no registrado.")
            return redirect('login')

    return render(request, 'login.html')
