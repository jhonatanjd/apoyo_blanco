from django.contrib import admin
from django.urls import path
from usuarios.views import *
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',Home, name="home"),
    path('quienes/',quienes, name="quienes"),
    path('ayuda/',ayuda, name="ayuda"),
    path('trabajar/',trabajar, name="trabajar"),
    path('Cardiología/',Cardiología, name="Cardiología"),
    path('Urgencias/',Urgencias, name="Urgencias"),
    path('familia/',familia, name="familia"),
    path('Geriatría/',Geriatría, name="Geriatría"),
    path('Neonatología/',Neonatología, name="Neonatología"),
    path('Nefrología/',Nefrología, name="Nefrología"),
    path('Oncología/',Oncología, name="Oncología"),
    path('Pediatría/',Pediatría, name="Pediatría"),
    path('primaria/',primaria, name="primaria"),
    path('escolar/',escolar, name="escolar"),
    path('mujer/',mujer, name="mujer"),
    path('cliente/',cliente, name="cliente"),
    path('profesional/',profesional, name="profesional"),
    path('terminos/',terminos, name="terminos"),
    path('rol_registro/',rol_registro, name="rol_registro"),
    path('rol_logueo/',rol_logueo, name="rol_logueo"),
    path('registro_usu/',registro_usu, name="registro_usu"),
    path('registro_prof/',registro_prof, name="registro_prof"),
    path('registrar_usuario/',registrar_usuario, name="registrar_usuario"),
    path('registrar_profesional/',registrar_profesional, name="registrar_profesional"),
    path('logueo_cliente/',logueo_cliente, name="logueo_cliente"),
    path('logueo_profesional/',logueo_profesional, name="logueo_profesional"),
    path('validacion_cliente/',validacion_cliente, name="validacion_cliente"),
    path('validacion_profesional/',validacion_profesional, name="validacion_profesional"),

]
