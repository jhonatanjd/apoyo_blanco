from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import *
from usuarios.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def Home (request):
    return render(request, 'home.html')

def ayuda (request):
    return render(request, 'ayuda.html')

def quienes (request):
    return render(request, 'quienes.html')

def Cardiología (request):
    return render(request, 'Cardiología.html')

def Urgencias (request):
    return render(request, 'Urgencias.html')

def familia (request):
    return render(request, 'familia.html')

def Geriatría (request):
    return render(request, 'Geriatría.html')

def Neonatología (request):
    return render(request, 'Neonatología.html')

def Nefrología (request):
    return render(request, 'Nefrología.html')

def Oncología (request):
    return render(request, 'Oncología.html')

def Pediatría (request):
    return render(request, 'Pediatría.html')

def primaria (request):
    return render(request, 'primaria.html')

def escolar (request):
    return render(request, 'escolar.html')

def mujer (request):
    return render(request, 'mujer.html')

def rol_registro (request):
    return render(request, 'rol.html')

def rol_logueo (request):
    return render(request, 'rol_logueo.html')

def terminos (request):
    return render(request, 'terminos.html')

def registro_usu (request):
    return render(request, 'registro_usuario.html')

def trabajar (request):
    return render(request, 'trabajar.html')

def registro_prof (request):
    return render(request, 'registro_profesional.html')


def registrar_profesional(request):
    if request.method == 'POST':
        form = registro_profesional(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.correo = form.cleaned_data['correo']
            var.password =make_password(form.cleaned_data['password'])
            var.nombres = form.cleaned_data['nombres']
            var.apellidos = form.cleaned_data['apellidos']
            var.cedula = form.cleaned_data['cedula']
            var.direccion = form.cleaned_data['direcion']
            var.telefono = form.cleaned_data['telefono']
            var.celular = form.cleaned_data['celular']
            var.grado_estudio= form.cleaned_data['grado_estudio']
            var.especialidad= form.cleaned_data['especialidad']
            var.ciudad = form.cleaned_data['ciudad']
            var.save()
            messages.success(request,'usuario cargado exitosamente!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form = registro_profesional ()
    return render (request,"registro_profesional.html",{'form': form})




def registrar_usuario(request):
    if request.method == 'POST':
        form = registro_usuarios(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = form.cleaned_data['username']
            var.password =make_password(form.cleaned_data['password'])
            var.nombres = form.cleaned_data['nombres']
            var.apellidos = form.cleaned_data['apellidos']
            var.cedula = form.cleaned_data['cedula']
            var.direccion = form.cleaned_data['direccion']
            var.telefono = form.cleaned_data['telefono']
            var.celular = form.cleaned_data['celular']
            var.correo = form.cleaned_data['correo']
            var.ciudad = form.cleaned_data['ciudad']
            var.save()
            messages.success(request,'usuario cargado exitosamente!!!')
        else:
            messages.warning(request,'Usuario no cargado')
    else:
        form = registro_usuarios ()
    
    return render (request,"registro_usuario.html",{'form': form})

def validacion_cliente(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')

        if cliente.objects.filter(username=user).exists():
            logueo=cliente.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo.html')
            else:
                request.session['seguridad']=True
                return render (request, 'cliente.html')
        else: 
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_cliente.html') 

def validacion_profesional(request):
    if request.method == 'POST':
        corre=request.POST.get('correo')
        passw=request.POST.get('password')

        if cliente.objects.filter(correo=corre).exists():
            logueo=cliente.objects.get(correo=corre)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo.html')
            else:
                request.session['seguridad']=True
                return render (request, 'profesional.html')
        else: 
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_profesional.html') 
        

def cliente (request):
    return render(request, 'cliente.html')

def profesional (request):
    return render(request, 'profesional.html')

def logueo_cliente (request):
    return render (request, 'logueo.html') 

def logueo_profesional (request):
    return render (request, 'logueo_profesional.html') 

def soporte (request):
    if request.method == 'POST':
        form = form_soporte(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.correo = form.cleaned_data['correo']
            var.comentario = form.cleaned_data['comentario'] 
            var.save()
            messages.success(request,'comentario cargado!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form = form_soporte() 
    return render (request,"ayuda.html",{'form': form})



