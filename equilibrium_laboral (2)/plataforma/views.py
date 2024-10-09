# plataforma/views.py

from firebase_admin import auth, firestore
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

# Definimos la función 'index'
def index(request):
    # Retornamos el renderizado de la plantilla 'inicio.html'
    return render(request, 'plataforma/index.html')

# Definimos la función 'perfil'
def perfil(request):
    # Retornamos el renderizado de la plantilla 'perfil.html'
    return render(request, 'plataforma/perfil.html')

# Definimos la Funcion Guardado de registro
def registro(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            # Crear usuario en Firebase Authentication
            user = auth.create_user(email=email, password=password)

            # Opcionalmente, también guarda información en Firestore
            db = firestore.client()
            user_ref = db.collection('users').document(user.uid)
            user_ref.set({
                'email': email,
                'uid': user.uid,
            })

            messages.success(request, "Usuario registrado exitosamente.")
            return redirect('login')  # Redirigir al login o a otra página
        except Exception as e:
            messages.error(request, f"Error registrando el usuario: {e}")
            return render(request, 'registro.html')
    
    return render(request, 'registro.html')

def login(request):
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

def test_firebase_auth(request):
    try:
        # Reemplaza este correo con uno que ya esté registrado en Firebase Authentication
        email = "usuario_prueba@ejemplo.com"
        
        # Obtener el usuario por correo
        user = auth.get_user_by_email(email)
        
        # Si la conexión es exitosa, retornamos detalles del usuario
        return JsonResponse({
            "uid": user.uid,
            "email": user.email,
            "mensaje": "Conexión con Firebase Authentication exitosa."
        })
    except Exception as e:
        return JsonResponse({
            "mensaje": "Error conectando con Firebase Authentication.",
            "error": str(e)
        })