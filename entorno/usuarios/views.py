from django.shortcuts import render

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import *
#from usuarios.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from .models import frutas
#from usuarios.models import frutas
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

def registro_usuario (request):
    return render(request, 'registro_usuario.html')

def trabajar (request):
    return render(request, 'trabajar.html')

def registro_profesional (request):
    return render(request, 'registro_profesional.html')

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



