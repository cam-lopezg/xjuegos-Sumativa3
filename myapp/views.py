from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from myapp.forms import CustomUserCreationForm, CustomUserChangeForm
from apiUsuarios.models import Usuario, TipoUsuario
from django.contrib.auth.hashers import check_password
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from apiProductos.models import Carrito, AuxCarritoProducto, Producto
from datetime import datetime, timedelta

User = get_user_model()
# Create your views here.

@login_required
def vista_restringida(request):
    # Tu lógica para la vista restringida aquí
    return render(request, 'vista_restringida.html')

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre').strip()
        username = request.POST.get('usuario').strip()
        password = request.POST.get('contrasena').strip()
        password2 = request.POST.get('contrasena2').strip()
        email = request.POST.get('email').strip()
        direccion = request.POST.get('direccion').strip()  # Campo opcional de dirección
        fecha_nacimiento = request.POST.get('nacimiento').strip()  # Ahora este campo es obligatorio

        # Inicia las validaciones
        errores = []

        # Validar que ningún campo obligatorio esté vacío
        campos = [nombre, username, password, password2, email, fecha_nacimiento]  # Incluye fecha de nacimiento
        nombres_campos = ["Nombre", "Nombre de usuario", "Contraseña", "Repetir contraseña", "Correo electrónico", "Fecha de nacimiento"]
        for campo, nombre_campo in zip(campos, nombres_campos):
            if not campo:
                errores.append(f"El campo {nombre_campo} no puede estar vacío.")

        # Continuar con las demás validaciones si no hay campos vacíos
        if not errores:
            # Verificar que las contraseñas coincidan y cumplan con las políticas
            if password != password2:
                errores.append("Las contraseñas deben ser iguales.")
            elif len(password) < 6 or len(password) > 18 or not any(char.isdigit() for char in password) or not any(char.isupper() for char in password):
                errores.append("La contraseña debe tener entre 6 y 18 caracteres, incluir al menos un número y una mayúscula.")

            # Verificar la edad mínima (13 años)
            try:
                nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
                edad_minima = datetime.now() - timedelta(days=13*365.25)
                if nacimiento > edad_minima:
                    errores.append("Debes tener al menos 13 años para registrarte.")
            except ValueError:
                errores.append("Formato de fecha de nacimiento inválido.")

            # Si no hay errores, proceder a crear el usuario
            if not errores:
                if User.objects.filter(nickname=username).exists():
                    errores.append("El nombre de usuario ya está en uso.")
                else:
                    user = User.objects.create_user(nombre=nombre, nickname=username, email=email, password=password, fecha_nacimiento= nacimiento)
                    user.direccion = direccion  # Guardar dirección en el perfil del usuario, asumiendo que ya existe el modelo relacionado
                    user.save()
                    django_login(request, user)
                    return redirect('home')

        # Si hay errores, retornar al formulario con los mensajes de error
        return render(request, 'Form.html', {'errores': errores})

    return render(request, 'Form.html')
    


@login_required
def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, 'create_user.html', {'form': form})

@login_required
def edit_user(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_user.html', {'form': form})

@login_required
def delete_user(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('home')  # Redirige a la página de inicio
    return render(request, 'delete_user.html')

def index(request):
    return render(request, 'principal.html')

def login(request):
    print("LOGIN VIEW")
    if request.method == 'POST':
        email = request.POST.get('username')  # Asegúrate de que el nombre del campo en tu formulario coincida
        password = request.POST.get('password')
        
        # Autenticar al usuario
        user = authenticate(request, username=email, password=password)  # Usa 'username' aunque sea el email
        if user is not None:
            # Usuario autenticado correctamente
            django_login(request, user)  # Inicia sesión al usuario
            print("Usuario autenticado")
            return redirect('home')  # Asegúrate de tener una URL con el nombre 'home'
        else:
            # Falló la autenticación
            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrecta.'
            })

    # Si no es una solicitud POST, simplemente renderiza la página de login
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')
    
def juego5dos(request):
    return render(request, 'juego5dos.html')

def juego5(request):
    return render(request, 'juego5.html')

def juego4dos(request):
    return render(request, 'juego4dos.html')

def juego4(request):
    return render(request, 'juego4.html')

def juego3dos(request):
    return render(request, 'juego3dos.html')

def juego3(request):
    return render(request, 'juego3.html')

def juego2dos(request):
    return render(request, 'juego2dos.html')

def juego2(request):
    return render(request, 'juego2.html')

def juego1dos(request):
    return render(request, 'juego1dos.html')

def juego1(request):
    return render(request, 'juego1.html')

def form(request):
    return render(request, 'Form.html')

def categoria5(request):
    return render(request, 'Categoria5.html')

def categoria4(request):
    return render(request, 'Categoria4.html')

def categoria3(request):
    return render(request, 'Categoria3.html')

def categoria2(request):
    return render(request, 'Categoria2.html')

def categoria1(request):
    return render(request, 'Categoria1.html')

def form_api(request):
     return render(request, 'RAWGAPI.html')
def form_api2(request):
     return render(request, 'BOMBAPI.html')

def carrito(request):
    usuario_id = request.user.id  # Asegúrate de que el usuario está autenticado
    carrito, created = Carrito.objects.get_or_create(usuario_id=usuario_id)

    productos_en_carrito = AuxCarritoProducto.objects.filter(carrito=carrito).select_related('producto')

    # Incluir el subtotal en el contexto
    items = [{
        'nombre': item.producto.nombre,
        'cantidad': item.cantidad,
        'precio': item.producto.precio,
        'subtotal': item.producto.precio * item.cantidad
    } for item in productos_en_carrito]

    total = sum(item['subtotal'] for item in items)

    context = {
        'productos': items,
        'total': total,
    }
    return render(request, 'carrito.html', context)

from django.http import HttpResponseRedirect
from django.urls import reverse

def limpiar_carrito(request):
    usuario_id = request.user.id
    carrito = Carrito.objects.get(usuario_id=usuario_id)
    AuxCarritoProducto.objects.filter(carrito=carrito).delete()
    return HttpResponseRedirect(reverse('carrito'))  # Redirige de nuevo a la vista del carrito

def pagar_carrito(request):
    usuario_id = request.user.id
    carrito = Carrito.objects.get(usuario_id=usuario_id)
    AuxCarritoProducto.objects.filter(carrito=carrito).delete()  # Opcionalmente vaciar el carrito
    return HttpResponseRedirect(reverse('carrito'))

from django.http import JsonResponse
from django.db.models import Sum


def obtener_cantidad_carrito(request):
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
        cantidad = AuxCarritoProducto.objects.filter(carrito=carrito).aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        return JsonResponse({'cantidad': cantidad})
    return JsonResponse({'cantidad': 0})

@login_required
def agregar_al_carrito(request):
    nombre_producto = request.GET.get('nombre')
    precio_producto = request.GET.get('precio', 0)

    # Buscar o crear el producto
    producto, created = Producto.objects.get_or_create(
        nombre=nombre_producto,
        defaults={'precio': precio_producto}
    )

    # Buscar o crear el carrito para el usuario actual
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)

    # Agregar el producto al carrito
    aux, created = AuxCarritoProducto.objects.get_or_create(carrito=carrito, producto=producto)
    print(aux)
    aux.cantidad += 1  # Ajusta la cantidad según sea necesario
    aux.save()

    # Redirigir al usuario al carrito
    return HttpResponseRedirect(reverse('home'))

def principal(request):
    return render (request, 'principal.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        nickname = request.POST['nickname']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = request.user
            user.nombre = nombre
            user.nickname = nickname
            user.email = email
            if password:  # Only update the password if one is provided
                user.password = make_password(password)
            user.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in after password change
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('edit_profile')
        except Exception as e:
            messages.error(request, 'Error al actualizar el perfil: {}'.format(e))

    return render(request, 'editarPerfil.html')

